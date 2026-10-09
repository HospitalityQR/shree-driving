/**
 * ============================================================================
 *  LOTUS HUT — THE DRIVE IN CAFE
 *  Central Configuration & Store Details
 * ============================================================================
 */

window.RESTAURANT_CONFIG = {
    // 1. Restaurant Brand Identity
    name: "LOTUS HUT",
    subname: "THE DRIVE IN CAFE",
    tagline: "Drive-In Dining • Gourmet Coffee • Fast Bites & Delicacies",
    highlight: "Pure Veg Delights • Fresh Roasted Coffee • Fast Car Service",
    city: "Indore",
    fullAddress: "Lotus Hut, The Drive In Cafe, Indore",
    
    // 2. Contact & Payment Numbers (As instructed by owner: 9111789220)
    phone: "9111789220",
    phoneDisplay: "+91 91117 89220",
    whatsappNumber: "919111789220", // WhatsApp international format
    
    // 3. Direct UPI Payment Details (9111789220)
    upiNumber: "9111789220",
    upiId: "9111789220-4@ybl",
    upiPayeeName: "ANSH CHHAJED",
    
    // 4. Hosted Landing Page & Live URL
    landingPageUrl: "https://hospitalityqr.github.io/shree-driving/?v=9",
    paymentPageUrl: "payment.html",
    
    // 5. Visual Media Assets
    logoUrl: "logo.png",
    boardNeonUrl: "board_neon.png",
    ambienceFrontUrl: "ambience_front.png",
    ambienceNightUrl: "ambience_night.png",
    
    // 6. Service Details
    defaultPrepTime: "15-20 Min",
    currency: "₹",
    allowCashAtCar: true, // Cash at Car Enabled
    allowDirectUpi: true,

    // 7. Instant Bank Verification Gateway (Razorpay)
    // NOTE: Only put your KYC-verified LIVE Key ID here (starts with "rzp_live_").
    // Leave empty ("") to use Direct PhonePe / GPay / Paytm & Dynamic QR Mode (prevents "Verification not done" error).
    razorpayKeyId: "",

    // 8. Staff Desk Strict Device Security PIN
    // Only authorized staff device with this PIN can unlock staff.html (Anti-Tamper)
    staffSecurityPin: "9111"
};
