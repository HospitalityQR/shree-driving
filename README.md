# 🚗 Lotus Hut — The Drive In Cafe
### Digital Menu, Direct UPI Payment (9111789220) & Two-Way WhatsApp Order Management System

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

- **Send Order via WhatsApp**:
  - Formats a clean WhatsApp message with Customer Name, Vehicle Number, Time, itemized bill, total amount, and direct **Staff Action Link**.
  - Sends directly to Lotus Hut WhatsApp **+91 91117 89220**.
  - Opens the **Live Order Tracking Sheet** on the customer's screen.

---

## 👨‍🍳 2. Owner & Service Man Control Portal (`staff.html`)

- **High-Visibility Vehicle Banner**:
  - Huge bold vehicle number badge so service staff can spot the car in the parking lot in seconds.

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
3. Open the cart, enter your Name and Vehicle Number (e.g. `MP 09 AB 1234`).
4. Inspect the dynamic UPI payment to **9111789220**.
5. Click **"Send Order via WhatsApp"** — notice the generated order format and live tracker!
6. Open **`staff.html`** — see the test order, click the **RED 🔴 Accept** button, watch it turn **GREEN ✅**, and test the **"Bill Push & All is Done"** button!
