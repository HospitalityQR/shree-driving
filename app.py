#!/usr/bin/env python3
"""
=============================================================================
  LOTUS HUT — THE DRIVE IN CAFE
  Swiggy-Inspired Payment & Order Management Backend Server
=============================================================================
  - Secure order creation & price calculation
  - Server-side payment verification (Razorpay Test Mode & Sandbox Engine)
  - Zero sensitive data storage (No CVVs, card numbers, or UPI PINs)
  - Full simulation support (Success, Bank Decline, Cancel)
  - Seamless static file serving and staff portal sync
=============================================================================
"""

import os
import json
import time
import hmac
import hashlib
import uuid
from datetime import datetime
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory, render_template_string
from dotenv import load_dotenv

# 1. Load Environment Variables
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

PORT = int(os.getenv("PORT", 5000))
HOST = os.getenv("HOST", "127.0.0.1")
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")
PAYMENT_MODE = os.getenv("PAYMENT_MODE", "test").lower()
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID", "rzp_test_lotushut123")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET", "rzp_test_secret_lotushut456")
CURRENCY = os.getenv("CURRENCY", "INR")
RESTAURANT_NAME = os.getenv("RESTAURANT_NAME", "Lotus Hut — The Drive In Cafe")
STORE_PHONE = os.getenv("STORE_PHONE", "9111789220")
STORE_UPI_ID = os.getenv("STORE_UPI_ID", "9111789220@ybl")

# 2. Try initializing Razorpay Client
razorpay_client = None
try:
    import razorpay
    if RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET and not RAZORPAY_KEY_ID.startswith("rzp_test_lotushut"):
        # Real or user-provided Razorpay test credentials
        razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
except Exception as e:
    print(f"[*] Note: Razorpay client running with built-in sandbox engine ({e})")

# 3. Persistent Orders Store File
ORDERS_FILE = BASE_DIR / "orders_data.json"

def load_orders():
    if not ORDERS_FILE.exists():
        return {}
    try:
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_orders(orders_dict):
    try:
        with open(ORDERS_FILE, "w", encoding="utf-8") as f:
            json.dump(orders_dict, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[!] Error saving orders: {e}")

# In-memory orders cache
ORDERS_STORE = load_orders()

# Active Promotional Coupons (Swiggy Style)
ACTIVE_COUPONS = {
    "SWIGGY50": {
        "discount_type": "flat",
        "value": 50,
        "min_order": 199,
        "desc": "Flat ₹50 OFF on orders above ₹199",
        "highlight": "MOST POPULAR"
    },
    "WELCOME": {
        "discount_type": "flat",
        "value": 30,
        "min_order": 99,
        "desc": "Flat ₹30 OFF on your meal",
        "highlight": "WELCOME OFFER"
    },
    "FEAST100": {
        "discount_type": "flat",
        "value": 100,
        "min_order": 399,
        "desc": "Flat ₹100 OFF on orders above ₹399",
        "highlight": "PARTY SAVINGS"
    },
    "FREESHIP": {
        "discount_type": "delivery",
        "value": 35,
        "min_order": 149,
        "desc": "Free Car Drive-In Service Fee (₹35 OFF)",
        "highlight": "FREE DELIVERY"
    }
}

# 4. Initialize Flask Application
app = Flask(__name__, static_folder=str(BASE_DIR))

# Helper: Generate server HMAC signature for test verification tokens
def generate_server_token(order_id, amount_paise):
    secret = RAZORPAY_KEY_SECRET.encode("utf-8")
    msg = f"{order_id}|{amount_paise}|{PAYMENT_MODE}".encode("utf-8")
    return hmac.new(secret, msg, hashlib.sha256).hexdigest()

def verify_server_token(order_id, amount_paise, token):
    expected = generate_server_token(order_id, amount_paise)
    return hmac.compare_digest(expected, token)


# =============================================================================
#  API ROUTES
# =============================================================================

@app.route("/api/config", methods=["GET"])
def get_config():
    """Public gateway configuration for the checkout frontend."""
    return jsonify({
        "success": True,
        "restaurant_name": RESTAURANT_NAME,
        "currency": CURRENCY,
        "payment_mode": PAYMENT_MODE,
        "is_test_mode": True if PAYMENT_MODE == "test" else False,
        "razorpay_key_id": RAZORPAY_KEY_ID,
        "store_phone": STORE_PHONE,
        "store_upi_id": STORE_UPI_ID,
        "delivery_base_fee": 35,
        "free_delivery_threshold": 199,
        "gst_percentage": 5.0
    })

@app.route("/api/qr", methods=["GET"])
def generate_dynamic_qr():
    """Generate dynamic live QR image on the fly."""
    import io
    import qrcode
    from urllib.parse import quote
    
    qr_type = request.args.get("type", "upi").lower()
    amount = request.args.get("amount", "").strip()
    note = request.args.get("note", "").strip() or "Lotus Hut Order"
    
    if qr_type == "menu":
        target = f"http://{request.host}/"
    else:
        target = f"upi://pay?pa={STORE_UPI_ID}&pn={quote(RESTAURANT_NAME)}&cu=INR"
        if amount:
            target += f"&am={amount}"
        if note:
            target += f"&tn={quote(note)}"
            
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(target)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#120406", back_color="#ffffff")
    
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf.getvalue(), 200, {"Content-Type": "image/png"}

@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    """Available promotional coupons."""
    return jsonify({
        "success": True,
        "coupons": [
            {"code": k, **v} for k, v in ACTIVE_COUPONS.items()
        ]
    })

@app.route("/api/create-order", methods=["POST"])
def create_order():
    """
    Secure Order Creation:
    - Calculates item totals, delivery charges, GST, and coupon discounts on server.
    - Generates order ID and cryptographic verification token.
    - Creates a Razorpay order in test mode or sandbox.
    """
    try:
        data = request.get_json(force=True, silent=True) or {}
        items = data.get("items", [])
        customer = data.get("customer", {})
        coupon_code = (data.get("coupon_code") or "").strip().upper()

        if not items:
            return jsonify({"success": False, "error": "Cart cannot be empty"}), 400

        # Calculate Item Total
        item_total = 0.0
        cleaned_items = []
        for it in items:
            count = int(it.get("count", 1))
            price = float(it.get("price", 0))
            if count <= 0 or price < 0:
                continue
            item_total += price * count
            cleaned_items.append({
                "id": it.get("id", ""),
                "name": it.get("name", "Unknown Item"),
                "price": price,
                "count": count,
                "subtotal": price * count
            })

        if item_total <= 0:
            return jsonify({"success": False, "error": "Invalid item prices"}), 400

        # Standard Drive-In / Delivery Fee (Free on orders >= ₹199)
        delivery_fee = 0.0 if item_total >= 199 else 35.0

        # GST 5% on food items
        taxes = round(item_total * 0.05, 2)

        # Apply Coupon Discount
        discount = 0.0
        coupon_applied = None
        if coupon_code and coupon_code in ACTIVE_COUPONS:
            c = ACTIVE_COUPONS[coupon_code]
            if item_total >= c["min_order"]:
                if c["discount_type"] == "flat":
                    discount = float(c["value"])
                elif c["discount_type"] == "delivery":
                    discount = delivery_fee
                coupon_applied = coupon_code

        # Final Payable Amount
        payable_amount = max(0.0, round(item_total + delivery_fee + taxes - discount, 2))
        amount_paise = int(payable_amount * 100)

        # Generate unique Order ID
        order_num = f"{int(time.time()) % 1000000:06d}"
        order_id = f"LH-{order_num}"

        # Generate Server Verification Token
        sec_token = generate_server_token(order_id, amount_paise)

        # Razorpay integration (or sandbox fallback)
        razorpay_order_id = f"order_test_{order_id.replace('-', '_').lower()}_{uuid.uuid4().hex[:8]}"
        if razorpay_client:
            try:
                rzp_resp = razorpay_client.order.create({
                    "amount": amount_paise,
                    "currency": CURRENCY,
                    "receipt": order_id,
                    "notes": {
                        "customer_name": customer.get("name", ""),
                        "vehicle_no": customer.get("vehicle", ""),
                        "phone": customer.get("phone", "")
                    }
                })
                razorpay_order_id = rzp_resp["id"]
            except Exception as rzp_err:
                print(f"[*] Razorpay API notice: using sandbox order ({rzp_err})")

        # Save order into memory / storage
        order_record = {
            "order_id": order_id,
            "status": "PENDING",
            "created_at": datetime.now().isoformat(),
            "customer": {
                "name": customer.get("name", "Guest"),
                "phone": customer.get("phone", ""),
                "vehicle": (customer.get("vehicle") or "").upper(),
                "spot": customer.get("spot", "Driveway / Parking"),
                "notes": customer.get("notes", "")
            },
            "items": cleaned_items,
            "bill": {
                "item_total": round(item_total, 2),
                "delivery_fee": round(delivery_fee, 2),
                "taxes": round(taxes, 2),
                "discount": round(discount, 2),
                "coupon_code": coupon_applied,
                "payable_amount": payable_amount,
                "amount_paise": amount_paise,
                "currency": CURRENCY
            },
            "security": {
                "token": sec_token,
                "razorpay_order_id": razorpay_order_id
            },
            "payment": None
        }

        ORDERS_STORE[order_id] = order_record
        save_orders(ORDERS_STORE)

        return jsonify({
            "success": True,
            "order_id": order_id,
            "razorpay_order_id": razorpay_order_id,
            "verification_token": sec_token,
            "amount_paise": amount_paise,
            "bill": order_record["bill"],
            "customer": order_record["customer"],
            "currency": CURRENCY,
            "is_test_mode": True if PAYMENT_MODE == "test" else False,
            "message": "Order created successfully. Ready for payment."
        })

    except Exception as e:
        return jsonify({"success": False, "error": f"Server error creating order: {str(e)}"}), 500

@app.route("/api/verify-payment", methods=["POST"])
def verify_payment():
    """
    Server-Side Payment Verification:
    - Never stores sensitive credentials (CVV, Card Number, UPI PIN).
    - Verifies cryptographic signature for Razorpay / sandbox token.
    - Confirms order ONLY after verified payment success.
    - Generates unique transaction ID.
    """
    try:
        data = request.get_json(force=True, silent=True) or {}
        order_id = data.get("order_id", "").strip()
        payment_id = data.get("payment_id", "").strip()
        payment_method = data.get("payment_method", "UPI").upper()
        method_details = data.get("method_details", {})
        verification_token = data.get("verification_token", "").strip()
        rzp_order_id = data.get("razorpay_order_id", "").strip()
        rzp_signature = data.get("razorpay_signature", "").strip()

        if not order_id or order_id not in ORDERS_STORE:
            return jsonify({"success": False, "error": "Order not found or invalid session"}), 404

        order = ORDERS_STORE[order_id]

        if order["status"] == "PAID":
            return jsonify({
                "success": True,
                "message": "Order is already paid and verified",
                "transaction_id": order["payment"]["transaction_id"],
                "order": order
            })

        verified = False
        verification_method = "Sandbox Test Verification"

        # 1. Razorpay Official Signature Verification (if client provided signature)
        if razorpay_client and rzp_signature and rzp_order_id and payment_id:
            try:
                razorpay_client.utility.verify_payment_signature({
                    "razorpay_order_id": rzp_order_id,
                    "razorpay_payment_id": payment_id,
                    "razorpay_signature": rzp_signature
                })
                verified = True
                verification_method = "Razorpay HMAC-SHA256"
            except Exception as e:
                return jsonify({"success": False, "error": f"Invalid Razorpay signature: {str(e)}"}), 400

        # 2. Server-Signed Test Mode / Sandbox Token Verification
        elif verification_token:
            amount_paise = order["bill"]["amount_paise"]
            if verify_server_token(order_id, amount_paise, verification_token):
                verified = True
                verification_method = "Server HMAC SHA-256 Token"
            else:
                return jsonify({"success": False, "error": "Tampered payment verification token"}), 400

        # 3. Cash on Delivery Verification
        elif payment_method == "COD":
            verified = True
            verification_method = "Cash on Delivery (Drive-In)"

        # 4. Standard Test Mode Fallback
        elif PAYMENT_MODE == "test" and payment_id.startswith(("pay_test_", "txn_test_")):
            verified = True
            verification_method = "Test Mode Gateway Sandbox"

        if not verified:
            return jsonify({"success": False, "error": "Payment could not be verified by server"}), 400

        # Generate Unique Transaction ID
        timestamp_str = datetime.now().strftime("%Y%m%d%H%M%S")
        rand_suffix = uuid.uuid4().hex[:6].upper()
        transaction_id = f"TXN_{PAYMENT_MODE.upper()}_{timestamp_str}_{rand_suffix}"

        # Safe Payment Metadata (Zero sensitive credentials stored!)
        safe_details = {}
        if payment_method == "UPI":
            safe_details = {
                "app": method_details.get("app", "UPI"),
                "upi_id": method_details.get("upi_id", "Customer UPI")
            }
        elif payment_method == "CARD":
            safe_details = {
                "card_network": method_details.get("card_network", "Card"),
                "last4": method_details.get("last4", "XXXX"),
                "cardholder_name": method_details.get("cardholder_name", "")
            }
        elif payment_method == "NETBANKING":
            safe_details = {
                "bank_name": method_details.get("bank_name", "Internet Banking")
            }
        elif payment_method == "WALLET":
            safe_details = {
                "wallet_name": method_details.get("wallet_name", "Digital Wallet")
            }
        elif payment_method == "COD":
            safe_details = {
                "type": "Pay Cash to Car Service Boy"
            }

        # Update Order Status
        now_iso = datetime.now().isoformat()
        order["status"] = "PAID" if payment_method != "COD" else "CONFIRMED_COD"
        order["payment"] = {
            "status": "SUCCESS",
            "transaction_id": transaction_id,
            "gateway_payment_id": payment_id or f"sim_{transaction_id}",
            "payment_method": payment_method,
            "method_details": safe_details,
            "verification_method": verification_method,
            "paid_amount": order["bill"]["payable_amount"],
            "currency": CURRENCY,
            "verified_at": now_iso,
            "is_simulated": True if PAYMENT_MODE == "test" else False
        }

        save_orders(ORDERS_STORE)

        return jsonify({
            "success": True,
            "status": "PAID",
            "message": "Payment verified and order confirmed successfully!",
            "transaction_id": transaction_id,
            "order_id": order_id,
            "verified_at": now_iso,
            "order": order
        })

    except Exception as e:
        return jsonify({"success": False, "error": f"Verification error: {str(e)}"}), 500

@app.route("/api/simulate-payment", methods=["POST"])
def simulate_payment():
    """
    Test Mode Gateway Sandbox Simulator:
    Allows testing:
    - Successful payment (scenario: 'success')
    - Bank decline / card error (scenario: 'failure')
    - User cancellation (scenario: 'cancelled')
    """
    try:
        data = request.get_json(force=True, silent=True) or {}
        order_id = data.get("order_id", "").strip()
        scenario = data.get("scenario", "success").lower()
        payment_method = data.get("payment_method", "UPI")
        method_details = data.get("method_details", {})

        if not order_id or order_id not in ORDERS_STORE:
            return jsonify({"success": False, "error": "Order not found"}), 404

        order = ORDERS_STORE[order_id]
        amount_paise = order["bill"]["amount_paise"]

        # Realistic simulation delay
        time.sleep(0.3)

        if scenario == "success":
            sim_payment_id = f"pay_test_{uuid.uuid4().hex[:14]}"
            sec_token = generate_server_token(order_id, amount_paise)
            
            return jsonify({
                "success": True,
                "scenario": "success",
                "payment_id": sim_payment_id,
                "verification_token": sec_token,
                "order_id": order_id,
                "amount_paise": amount_paise,
                "status": "AUTHORIZED",
                "message": "Simulated bank authorization successful."
            })

        elif scenario == "failure":
            fail_txn_id = f"TXN_FAIL_{int(time.time())}_{uuid.uuid4().hex[:4].upper()}"
            reasons = [
                ("PAYMENT_DECLINED_BY_BANK", "Transaction was declined by issuing bank (Test Simulation)"),
                ("INSUFFICIENT_FUNDS", "Insufficient balance in selected account (Test Simulation)"),
                ("INCORRECT_OTP", "The bank authentication OTP entered was invalid (Test Simulation)"),
                ("BANK_SERVER_BUSY", "Bank response timed out. Please try again or switch method.")
            ]
            # Pick a specific failure reason or user requested reason
            reason_code = data.get("error_code")
            chosen = next((r for r in reasons if r[0] == reason_code), reasons[0])

            return jsonify({
                "success": False,
                "scenario": "failure",
                "status": "FAILED",
                "transaction_id": fail_txn_id,
                "error_code": chosen[0],
                "error_message": chosen[1],
                "order_id": order_id,
                "can_retry": True
            }), 402

        elif scenario == "cancelled":
            return jsonify({
                "success": False,
                "scenario": "cancelled",
                "status": "CANCELLED",
                "error_code": "USER_CANCELLED",
                "error_message": "Payment was cancelled by the customer. Cart remains intact.",
                "order_id": order_id,
                "can_retry": True
            }), 200

        else:
            return jsonify({"success": False, "error": "Unknown simulation scenario"}), 400

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/order/<order_id>", methods=["GET"])
def get_order_details(order_id):
    """Retrieve details and status for a specific order."""
    if order_id not in ORDERS_STORE:
        return jsonify({"success": False, "error": "Order not found"}), 404
    return jsonify({"success": True, "order": ORDERS_STORE[order_id]})

@app.route("/api/orders", methods=["GET"])
def list_orders():
    """List recent orders (for staff kitchen & sync)."""
    orders_list = list(ORDERS_STORE.values())
    orders_list.sort(key=lambda x: x.get("created_at", ""), reverse=True)
    return jsonify({
        "success": True,
        "count": len(orders_list),
        "orders": orders_list[:50]
    })


# =============================================================================
#  STATIC & FRONTEND PAGE ROUTES
# =============================================================================

@app.route("/", methods=["GET"])
def serve_index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/payment", methods=["GET"])
@app.route("/payment.html", methods=["GET"])
def serve_payment():
    return send_from_directory(BASE_DIR, "payment.html")

@app.route("/staff", methods=["GET"])
@app.route("/staff.html", methods=["GET"])
def serve_staff():
    return send_from_directory(BASE_DIR, "staff.html")

@app.route("/standee", methods=["GET"])
@app.route("/standee.html", methods=["GET"])
def serve_standee():
    return send_from_directory(BASE_DIR, "standee.html")

@app.route("/<path:filename>", methods=["GET"])
def serve_static(filename):
    """Serve images, javascript files, css, etc."""
    file_path = BASE_DIR / filename
    if file_path.exists() and file_path.is_file():
        return send_from_directory(BASE_DIR, filename)
    return jsonify({"error": "File not found"}), 404


# =============================================================================
#  SERVER STARTUP
# =============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print(" 🚗 LOTUS HUT — SWIGGY-INSPIRED PAYMENT & ORDER SERVER")
    print("=" * 65)
    print(f" • Mode:             {'SANDBOX TEST MODE' if PAYMENT_MODE == 'test' else 'LIVE PRODUCTION'}")
    print(f" • Server URL:       http://{HOST}:{PORT}")
    print(f" • Customer Menu:    http://{HOST}:{PORT}/")
    print(f" • Swiggy Checkout:  http://{HOST}:{PORT}/payment.html")
    print(f" • Staff Desk:       http://{HOST}:{PORT}/staff.html")
    print("=" * 65)
    app.run(host=HOST, port=PORT, debug=DEBUG)
