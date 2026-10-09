# 🚗 Lotus Hut — The Drive In Cafe
### Digital Menu, Direct UPI Payment (9111789220) & Two-Way WhatsApp Order Management System

---

## 🌐 Live URLs:
- 📱 **Customer Digital Menu**: https://hospitalityqr.github.io/shree-driving/
- 👨‍🍳 **Staff & Kitchen Portal**: https://hospitalityqr.github.io/shree-driving/staff.html
- 🖼️ **Printable Standee**: https://hospitalityqr.github.io/shree-driving/standee.html

---

## 🌟 Overview & Key Features

This system is built specifically for **Lotus Hut — The Drive In Cafe** matching the uploaded ambience and neon signboard branding. It allows car passengers and drive-in visitors to view the luxury menu, place orders to their vehicle, pay via UPI, and enables the owner/serviceman to accept and fulfill orders with automatic WhatsApp status updates.

---

## 📱 1. Customer Ordering App (`index.html`)

- **Luxury Visual Design**:
  - Dark obsidian and glowing neon crimson theme matching the Lotus Hut night drive-in driveway & neon board.
  - Official Lotus Hut coffee cup logo with 24K gold foil trim and glassmorphism.
  - Ultra-fast & mobile-responsive so customers can browse effortlessly from inside their vehicle.

- **Menu & Real-Time Cart Calculation**:
  - Filter by categories: *Coffee & Sips*, *Thick Shakes*, *Burgers & Sandwiches*, *Pizzas & Breads*, *Loaded Fries & Bites*, *Chinese & Starters*, *Paneer & Tandoor*, *Main Course & Dal*, *Desserts*.
  - Instant live dish search.
  - Floating bottom tray displays **total items** and **live total price (₹ Total)**.

- **Mandatory Vehicle & Customer Details**:
  - **Customer Name**
  - **Vehicle Number** (e.g. `MP 09 AB 1234` — prominently formatted for quick spot by service boys)
  - Parking Spot / Bay No.
  - Phone Number & Cooking Requests (optional)

- **Direct UPI Payment (9111789220)**:
  - Exact order amount dynamic UPI QR Code generated instantly.
  - 1-Click **"Pay via UPI App"** launcher (Google Pay, PhonePe, Paytm, BHIM).
  - 1-Click Copy button for `9111789220`.
  - Payment mode options: *UPI Paid (9111789220)* or *Pay Cash at Car*.

- **Swiggy/Zomato Auto-Confirm & Instant WhatsApp Dispatch**:
  - Automatically verifies online prepaid transactions.
  - Automatically sends order slip directly to cafe WhatsApp (+91 91117 89220).
  - **Zero Staff Links Exposed**: Staff action links are removed from customer WhatsApp receipts so customers cannot access or tamper with internal staff controls.
  - Required 10-digit WhatsApp phone and vehicle validation prevents fake/spam orders.

---

## 👨‍🍳 2. Owner & Service Man Control Portal (`staff.html`)

- **Strict Device Security & 4-Digit Staff PIN (Default: `9111`)**:
  - Terminal is protected behind an anti-tamper security PIN lock screen.
  - Only authorized staff devices (kitchen counter phone / POS) with PIN can unlock and view orders.
  - Rate limiting protects against unauthorized PIN guessing (lockout after 5 wrong attempts).
  - 1-Click "Lock Desk" button locks the terminal when staff steps away.
  - URL parameter tampering is blocked unless unlocked.
  - Each order carries an authenticated security hash to prevent counterfeit orders.

- **High-Visibility Vehicle Banner**:
  - Huge bold vehicle number badge so service staff can spot the car in the parking lot in seconds.
  - Click-to-call customer phone link for instant car spot verification.

- **Stage 1: Acceptance Workflow**:
  - When a new order arrives, the button is **RED 🔴: [ 🔴 Accept Order (स्वीकार करें) ]**.
  - When clicked by owner or serviceman:
    - Button instantly morphs into **GREEN ✅: [ ✅ Order Accepted ]**.
    - Plays a sound chime.
    - Prepares & opens WhatsApp confirmation back to the customer:
      `"Namaste [Name] ji! Your order for Vehicle [Vehicle No] has been ACCEPTED! 👨‍🍳 Chef is preparing your fresh meal (~15-20 min)."`
    - Syncs live to the customer's phone screen!

- **Stage 2: Bill Push & Ready Workflow**:
  - After acceptance, the button **[ 🧾 Bill Push & Mark Ready (तैयार है) ]** activates.
  - When clicked:
    - Button turns **EMERALD GREEN ✅: [ ✅ All is Done (Served at Car) 🚗✨ ]**.
    - Plays victory chime.
    - Prepares & sends customer WhatsApp notification:
      `"Namaste [Name] ji! ALL IS DONE! Your order for Vehicle [Vehicle No] is READY! Our service man is serving it right at your car. 🚗✨"`

- **Print KOT & Thermal Receipts**:
  - 1-Click printable Kitchen Order Ticket (KOT) format for kitchen and counter records.

---

## 💳 3. Swiggy-Inspired Secure Payment Feature (`payment.html` & `app.py`)

- **Modern Swiggy Checkout UI/UX**:
  - Clean orange-and-white theme (`#fc8019`), card-based layout, and mobile-friendly responsive design.
  - Transparent item breakdown, live quantity controls (`+` / `-`), taxes (5% GST), and drive-in service fee.
  - Interactive coupon engine (`SWIGGY50`, `WELCOME`, `FEAST100`, `FREESHIP`) with instant savings highlights.
- **5 Comprehensive Payment Methods**:
  1. **UPI**: Google Pay, PhonePe, Paytm, and custom UPI ID validation with instant handle chips (`@okhdfcbank`, `@okaxis`, `@okicici`, `@oksbi`, `@paytm`, `@ybl`).
  2. **Credit & Debit Cards**: Real-time card formatting, brand recognition (Visa, Mastercard, RuPay, Amex), expiry auto-slash, CVV masking with 256-bit SSL guarantee.
  3. **Net Banking**: 6 popular Indian bank choices (HDFC, SBI, ICICI, Axis, Kotak, PNB) + dropdown for 40+ banks.
  4. **Digital Wallets**: Amazon Pay, Paytm Wallet, PhonePe Wallet, Mobikwik.
  5. **Cash on Delivery (COD)**: Pay cash to car service boy with anti-bot 3-digit security verification code.
- **Payment Statuses & Animations**:
  - **Processing Radar**: Real-time pulsing bank gateway authorization screen.
  - **Success Screen**: Animated SVG green checkmark, celebratory 4-note ascending chime, unique transaction ID (`TXN_TEST_...`), 1-click WhatsApp order slip, and printable receipt.
  - **Failure Screen**: Explanatory decline reasons, unique failure reference, and "🔄 Retry Payment" button (keeps cart intact).
- **Secure Backend APIs (`app.py`)**:
  - `POST /api/create-order`: Calculates order total, taxes, delivery fee, coupons, generates HMAC server token.
  - `POST /api/verify-payment`: Verifies Razorpay HMAC signature or server token, generates unique transaction ID, marks order confirmed.
  - `POST /api/simulate-payment`: Sandbox testing for successful, bank decline, and cancelled transactions.
  - `GET /api/config` & `GET /api/coupons`: Public gateway configuration.
  - **Zero credential storage**: Never stores card numbers, CVVs, or UPI PINs.

---

## 🚀 How to Run & Test

### Option A: Complete Backend Server (Recommended)
1. Double-click **`run_server.bat`** (or run `python app.py`).
2. Server starts at `http://127.0.0.1:5000`.
3. The Swiggy Payment Page opens automatically at `http://127.0.0.1:5000/payment.html`.
4. Test the bottom floating **Sandbox Controls**:
   - Click **🟢 Test Success** to test the green checkmark, unique transaction ID, and staff sync.
   - Click **🔴 Test Bank Decline** to test the failure screen and Retry button.
   - Click **🟡 Test Cancel** to test user cancellation.
5. Place an order and check `http://127.0.0.1:5000/staff.html` (PIN: `9111`) to watch the order arrive in real-time!

### Option B: Standalone Browser Testing
1. Double-click **`launch.bat`** (opens `payment.html`, `index.html`, and `staff.html` in your browser).
2. Enjoy the full frontend simulation with local state persistence and audio chime.

