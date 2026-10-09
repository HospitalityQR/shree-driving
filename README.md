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

## 🚀 How to Run & Test

1. Double-click **`launch.bat`** (or open `index.html` in your browser).
2. Select any dishes from the menu to see the floating cart and total calculation.
3. Open the tray, enter Name, Vehicle Number, and 10-Digit WhatsApp Mobile No.
4. Click **"Pay & Place Order"** — experience the Swiggy/Zomato style bank radar, automatic green checkmark confirmation, and automatic WhatsApp message opening!
5. Open **`staff.html`** on the counter phone — enter Staff PIN **`9111`** to unlock the secure terminal, manage orders, and test the red/green stage buttons!
