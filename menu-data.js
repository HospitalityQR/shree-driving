/**
 * ============================================================================
 *  LOTUS HUT — THE DRIVE IN CAFE
 *  Complete Digital Menu Database
 * ============================================================================
 */

var MENU_CATEGORIES = [
    { id: "all", name: "All Items", icon: "✨" },
    { id: "coffee", name: "Coffee & Sips", icon: "☕" },
    { id: "shakes", name: "Thick Shakes", icon: "🥤" },
    { id: "burgers", name: "Burgers & Sandwiches", icon: "🍔" },
    { id: "pizza", name: "Pizzas & Breads", icon: "🍕" },
    { id: "bites", name: "Loaded Fries & Bites", icon: "🍟" },
    { id: "chinese", name: "Chinese & Starters", icon: "🥢" },
    { id: "tandoor", name: "Paneer & Tandoor", icon: "🍢" },
    { id: "maincourse", name: "Main Course & Dal", icon: "🍛" },
    { id: "desserts", name: "Desserts & Ice Cream", icon: "🍨" }
];

var MENU_DATA = [
    // -------------------------------------------------------------------------
    // 1. COFFEE & HOT SIPS ☕
    // -------------------------------------------------------------------------
    {
        id: "cf_1",
        name: "Lotus Special Cold Coffee with Ice Cream",
        nameHi: "लोटस स्पेशल कोल्ड कॉफी विथ आइसक्रीम",
        category: "coffee",
        price: 150,
        badge: "Bestseller",
        desc: "Thick blended Arabica brew topped with rich vanilla scoop and chocolate drizzle.",
        prepTime: "5-10 Min",
        isVeg: true
    },
    {
        id: "cf_2",
        name: "Classic Cold Coffee",
        nameHi: "क्लासिक कोल्ड कॉफी",
        category: "coffee",
        price: 120,
        badge: "Popular",
        desc: "Refreshing creamy frappe made with fresh milk and roasted espresso blend.",
        prepTime: "5-10 Min",
        isVeg: true
    },
    {
        id: "cf_3",
        name: "Hazelnut Cold Coffee",
        nameHi: "हेज़लनट कोल्ड कॉफी",
        category: "coffee",
        price: 160,
        badge: "Chef Special",
        desc: "Premium roasted hazelnut infused chilled coffee with thick creamy foam.",
        prepTime: "5-10 Min",
        isVeg: true
    },
    {
        id: "cf_4",
        name: "Hot Cappuccino",
        nameHi: "हॉट कैपुचीनो",
        category: "coffee",
        price: 90,
        desc: "Steaming hot espresso topped with rich velvety milk froth.",
        prepTime: "5 Min",
        isVeg: true
    },
    {
        id: "cf_5",
        name: "Hot Chocolate Fudge",
        nameHi: "हॉट चॉकलेट फज",
        category: "coffee",
        price: 130,
        desc: "Rich dark Belgian cocoa simmered with sweet milk.",
        prepTime: "5-10 Min",
        isVeg: true
    },
    {
        id: "cf_6",
        name: "Special Desi Masala Chai",
        nameHi: "स्पेशल मसाला चाय (कुल्हड़)",
        category: "coffee",
        price: 40,
        badge: "Highway Special",
        desc: "Traditional highway tea brewed with ginger, cardamom, and secret spices.",
        prepTime: "5 Min",
        isVeg: true
    },

    // -------------------------------------------------------------------------
    // 2. THICK SHAKES & COOLERS 🥤
    // -------------------------------------------------------------------------
    {
        id: "sh_1",
        name: "KitKat Crunch Shake",
        nameHi: "किटकेट क्रंच शेक",
        category: "shakes",
        price: 170,
        badge: "Bestseller",
        desc: "Rich chocolate thickshake blended with crunchy KitKat bars and wafers.",
        prepTime: "5-10 Min",
        isVeg: true
    },
    {
        id: "sh_2",
        name: "Oreo Mudslide Shake",
        nameHi: "ओरियो मडस्लाइड शेक",
        category: "shakes",
        price: 160,
        badge: "Must Try",
        desc: "Crunchy Oreo cookies whipped into double chocolate dairy shake.",
        prepTime: "5-10 Min",
        isVeg: true
    },
    {
        id: "sh_3",
        name: "Brownie Blast Shake",
        nameHi: "ब्राउनी ब्लास्ट शेक",
        category: "shakes",
        price: 180,
        badge: "Chef Special",
        desc: "Loaded with fresh chocolate brownie chunks, dark chocolate and choco chips.",
        prepTime: "5-10 Min",
        isVeg: true
    },
    {
        id: "sh_4",
        name: "Fresh Mango Thickshake",
        nameHi: "मैंगो थिकशेक",
        category: "shakes",
        price: 160,
        desc: "Alphonso mango pulp blended with rich dairy ice cream.",
        prepTime: "5-10 Min",
        isVeg: true
    },
    {
        id: "sh_5",
        name: "Virgin Mint Mojito",
        nameHi: "वर्जिन मिंट मोजितो",
        category: "shakes",
        price: 130,
        desc: "Chilled sparkling soda with fresh crushed garden mint leaves, lime and ice.",
        prepTime: "5 Min",
        isVeg: true
    },
    {
        id: "sh_6",
        name: "Blue Curacao Sparkler",
        nameHi: "ब्लू कुराकाओ स्पार्क्लर",
        category: "shakes",
        price: 140,
        desc: "Vibrant tropical blue citrus cooler served over ice crystals.",
        prepTime: "5 Min",
        isVeg: true
    },

    // -------------------------------------------------------------------------
    // 3. BURGERS & SANDWICHES 🍔
    // -------------------------------------------------------------------------
    {
        id: "bg_1",
        name: "Lotus Crispy Veg Burger",
        nameHi: "लोटस क्रिस्पी वेज बर्गर",
        category: "burgers",
        price: 110,
        badge: "Bestseller",
        desc: "Crispy herb potato patty, fresh tomatoes, lettuce and house signature mayo sauce.",
        prepTime: "10-15 Min",
        isVeg: true
    },
    {
        id: "bg_2",
        name: "Paneer Makhani Cheese Burger",
        nameHi: "पनीर मखानी चीज़ बर्गर",
        category: "burgers",
        price: 160,
        badge: "Chef Special",
        desc: "Thick grilled cottage cheese slab glazed with rich buttery makhani gravy and cheddar.",
        prepTime: "10-15 Min",
        isVeg: true
    },
    {
        id: "bg_3",
        name: "Double Cheese Jumbo Tower Burger",
        nameHi: "डबल चीज़ जंबो बर्गर",
        category: "burgers",
        price: 180,
        badge: "Must Try",
        desc: "Dual crispy patties layered with melt cheese slice, pickled onion and spicy relish.",
        prepTime: "10-15 Min",
        isVeg: true
    },
    {
        id: "bg_4",
        name: "Bombay Masala Grilled Sandwich",
        nameHi: "बॉम्बे मसाला ग्रिल्ड सैंडविच",
        category: "burgers",
        price: 140,
        badge: "Popular",
        desc: "Triple layer bread filled with spiced aloo masala, crunchy veggies, and mint chutney.",
        prepTime: "10-15 Min",
        isVeg: true
    },
    {
        id: "bg_5",
        name: "Cheese Corn Capsicum Grilled Sandwich",
        nameHi: "चीज़ कॉर्न ग्रिल्ड सैंडविच",
        category: "burgers",
        price: 160,
        desc: "Golden sweet corn and crisp bell peppers loaded with 100% mozzarella and grilled crisp.",
        prepTime: "10-15 Min",
        isVeg: true
    },
    {
        id: "bg_6",
        name: "Paneer Tikka Club Sandwich",
        nameHi: "पनीर टिक्का क्लब सैंडविच",
        category: "burgers",
        price: 180,
        badge: "Drive-In King",
        desc: "Smoky tandoori paneer slices with layered creamy cheese, greens and tandoori spread.",
        prepTime: "10-15 Min",
        isVeg: true
    },

    // -------------------------------------------------------------------------
    // 4. PIZZAS & BREADS 🍕
    // -------------------------------------------------------------------------
    {
        id: "pz_1",
        name: "Margherita Supreme Pizza (8 Inch)",
        nameHi: "मार्गेरीटा सुप्रीम पिज़्ज़ा",
        category: "pizza",
        price: 220,
        badge: "Classic",
        desc: "Classic Italian marinara, fragrant basil herbs, and overflowing mozzarella cheese.",
        prepTime: "15-20 Min",
        isVeg: true
    },
    {
        id: "pz_2",
        name: "Paneer Tikka Highway Pizza (8 Inch)",
        nameHi: "पनीर टिक्का हाईवे पिज़्ज़ा",
        category: "pizza",
        price: 280,
        badge: "Bestseller",
        desc: "Marinated spicy paneer cubes, roasted capsicum, onion flakes, and garlic herbs.",
        prepTime: "15-20 Min",
        isVeg: true
    },
    {
        id: "pz_3",
        name: "Lotus Farmhouse Feast Pizza (8 Inch)",
        nameHi: "लोटस फार्महाउस फीस्ट पिज़्ज़ा",
        category: "pizza",
        price: 290,
        badge: "Chef Special",
        desc: "Loaded with black olives, golden corn, mushrooms, bell peppers and liquid cheddar.",
        prepTime: "15-20 Min",
        isVeg: true
    },
    {
        id: "pz_4",
        name: "Stuffed Cheese Garlic Bread (4 Pcs)",
        nameHi: "स्टफ्ड चीज़ गार्लिक ब्रेड",
        category: "pizza",
        price: 160,
        desc: "Crispy herb crusted loaf stuffed with garlic butter, sweet corn, and stretchy cheese.",
        prepTime: "10-15 Min",
        isVeg: true
    },

    // -------------------------------------------------------------------------
    // 5. LOADED FRIES & BITES 🍟
    // -------------------------------------------------------------------------
    {
        id: "bt_1",
        name: "French Fries Classic Salted",
        nameHi: "क्लासिक साल्टेड फ्रेंच फ्राइज",
        category: "bites",
        price: 110,
        desc: "Crispy golden cut potato batons tossed in sea salt.",
        prepTime: "10 Min",
        isVeg: true
    },
    {
        id: "bt_2",
        name: "Peri Peri Masala Fries",
        nameHi: "पेरी पेरी मसाला फ्राइज",
        category: "bites",
        price: 130,
        badge: "Bestseller",
        desc: "Crispy fries shaken with tangy spicy African peri peri seasoning.",
        prepTime: "10 Min",
        isVeg: true
    },
    {
        id: "bt_3",
        name: "Cheesy Overloaded Fries",
        nameHi: "चीज़ी ओवरलोडेड फ्राइज",
        category: "bites",
        price: 170,
        badge: "Must Try",
        desc: "Crispy fries smothered in liquid warm cheddar, mozzarella and jalapeño bits.",
        prepTime: "10-15 Min",
        isVeg: true
    },
    {
        id: "bt_4",
        name: "Crispy Corn Salt & Pepper",
        nameHi: "क्रिस्पी कॉर्न साल्ट & पेपर",
        category: "bites",
        price: 180,
        desc: "Golden sweet corn fried to crackling crisp and tossed with onion, lemon and pepper.",
        prepTime: "10-15 Min",
        isVeg: true
    },
    {
        id: "bt_5",
        name: "Cheese Cigar Rolls (8 Pcs)",
        nameHi: "चीज़ सिगार रोल (8 नग)",
        category: "bites",
        price: 260,
        badge: "Star Starter",
        desc: "Crunchy phyllo rolls stuffed with molten cheese and served with hot salsa dip.",
        prepTime: "10-15 Min",
        img: "assets/food_cheese_cigar.jpg",
        isVeg: true
    },

    // -------------------------------------------------------------------------
    // 6. CHINESE & STARTERS 🥢
    // -------------------------------------------------------------------------
    {
        id: "ch_1",
        name: "Veg Hakka Noodles",
        nameHi: "वेज हक्का नूडल्स",
        category: "chinese",
        price: 180,
        badge: "Popular",
        desc: "Wok tossed noodles with shredded cabbage, bell peppers and mild seasoning.",
        prepTime: "15 Min",
        isVeg: true
    },
    {
        id: "ch_2",
        name: "Chilli Garlic Noodles",
        nameHi: "चिली गार्लिक नूडल्स",
        category: "chinese",
        price: 200,
        desc: "Spicy noodles cooked with crushed burnt garlic and red chilli sauce.",
        prepTime: "15 Min",
        isVeg: true
    },
    {
        id: "ch_3",
        name: "Veg Manchurian (Dry / Gravy)",
        nameHi: "वेज मंचूरियन",
        category: "chinese",
        price: 190,
        badge: "Bestseller",
        desc: "Savory veggie dumplings tossed in ginger garlic soya glaze.",
        prepTime: "15 Min",
        img: "assets/food_manchurian.jpg",
        isVeg: true
    },
    {
        id: "ch_4",
        name: "Chilli Paneer (Dry)",
        nameHi: "चिल्ली पनीर (ड्राई)",
        category: "chinese",
        price: 260,
        badge: "Chef Special",
        desc: "Crispy fresh paneer cubes wok tossed with crunchy onions, capsicum and dark soya.",
        prepTime: "15-20 Min",
        img: "assets/food_chinese.jpg",
        isVeg: true
    },
    {
        id: "ch_5",
        name: "Honey Chilli Potato",
        nameHi: "हनी चिली पोटैटो",
        category: "chinese",
        price: 210,
        desc: "Crispy finger potatoes tossed in sweet chilli honey glaze and roasted sesame.",
        prepTime: "15 Min",
        isVeg: true
    },
    {
        id: "ch_6",
        name: "Crispy Spring Rolls",
        nameHi: "क्रिस्पी स्प्रिंग रोल",
        category: "chinese",
        price: 220,
        desc: "Golden fried sheets rolled with spiced seasonal vegetable juliennes.",
        prepTime: "15 Min",
        isVeg: true
    },

    // -------------------------------------------------------------------------
    // 7. PANEER & TANDOOR SPECIALS 🍢
    // -------------------------------------------------------------------------
    {
        id: "tn_1",
        name: "Paneer Tikka (Tandoori)",
        nameHi: "पनीर टिक्का (तंदूरी)",
        category: "tandoor",
        price: 280,
        badge: "Bestseller",
        desc: "Pure malai paneer steeped in mustard hung curd marinade, char-grilled to perfection.",
        prepTime: "15-20 Min",
        img: "assets/food_paneer.jpg",
        isVeg: true
    },
    {
        id: "tn_2",
        name: "Malai Paneer Tikka",
        nameHi: "मलाई पनीर टिक्का",
        category: "tandoor",
        price: 300,
        badge: "Royal Taste",
        desc: "Melt-in-mouth cottage cheese marinated with cashew paste, cardamom and rich cream.",
        prepTime: "15-20 Min",
        isVeg: true
    },
    {
        id: "tn_3",
        name: "Tandoori Malai Soya Chaap",
        nameHi: "तंदूरी मलाई सोया चाप",
        category: "tandoor",
        price: 260,
        desc: "Juicy soya chaap char-grilled with butter, fresh cream and aromatic spices.",
        prepTime: "15-20 Min",
        isVeg: true
    },
    {
        id: "tn_4",
        name: "Lotus Grand Platter",
        nameHi: "लोटस ग्रांड प्लेटर",
        category: "tandoor",
        price: 450,
        badge: "King Special",
        desc: "Festive assortment of Paneer Tikka, Veg Kabab, Cheese Cigars and Tandoori Chaap.",
        prepTime: "20 Min",
        img: "assets/food_platter.jpg",
        isVeg: true
    },

    // -------------------------------------------------------------------------
    // 8. MAIN COURSE & DAL 🍛
    // -------------------------------------------------------------------------
    {
        id: "mc_1",
        name: "Paneer Butter Masala",
        nameHi: "पनीर बटर मसाला",
        category: "maincourse",
        price: 280,
        badge: "Bestseller",
        desc: "Soft cottage cheese simmered in velvety tomato gravy with pure butter and spices.",
        prepTime: "20 Min",
        img: "assets/food_paneer.jpg",
        isVeg: true
    },
    {
        id: "mc_2",
        name: "Shahi Kaju Curry",
        nameHi: "शाही काजू करी",
        category: "maincourse",
        price: 320,
        badge: "Royal Rich",
        desc: "Whole fried cashew nuts tossed in rich cream and brown onion gravy.",
        prepTime: "20 Min",
        isVeg: true
    },
    {
        id: "mc_3",
        name: "Dal Makhani (Slow Cooked)",
        nameHi: "दाल मखानी (स्लो कुक्ड)",
        category: "maincourse",
        price: 240,
        badge: "Desi Ghee",
        desc: "Overnight slow cooked black lentils enriched with butter, cream, and smoky aroma.",
        prepTime: "15-20 Min",
        img: "assets/food_dal_tadka.jpg",
        isVeg: true
    },
    {
        id: "mc_4",
        name: "Dal Tadka (Desi Ghee)",
        nameHi: "दाल तड़का (देशी घी)",
        category: "maincourse",
        price: 190,
        desc: "Yellow arhar dal tempered with cumin, burnt garlic and whole red chillies in ghee.",
        prepTime: "15 Min",
        img: "assets/food_dal_tadka.jpg",
        isVeg: true
    },
    {
        id: "mc_5",
        name: "Butter Naan / Garlic Naan",
        nameHi: "बटर नान / गार्लिक नान",
        category: "maincourse",
        price: 60,
        desc: "Clay oven baked leavened bread brushed with amul butter or crushed garlic.",
        prepTime: "10 Min",
        img: "assets/food_naan.jpg",
        isVeg: true
    },
    {
        id: "mc_6",
        name: "Jeera Basmati Rice",
        nameHi: "जीरा बासमती राइस",
        category: "maincourse",
        price: 180,
        desc: "Fragrant long grain basmati rice tossed with roasted cumin seeds and fresh coriander.",
        prepTime: "15 Min",
        isVeg: true
    },

    // -------------------------------------------------------------------------
    // 9. DESSERTS & ICE CREAMS 🍨
    // -------------------------------------------------------------------------
    {
        id: "ds_1",
        name: "Sizzling Brownie with Vanilla Scoop",
        nameHi: "सिजलिंग ब्राउनी विथ वैनिला आइसक्रीम",
        category: "desserts",
        price: 190,
        badge: "Bestseller",
        desc: "Hot walnut brownie on a smoking cast iron platter with vanilla scoop and hot fudge.",
        prepTime: "10 Min",
        isVeg: true
    },
    {
        id: "ds_2",
        name: "Gulab Jamun with Ice Cream (2 Pcs)",
        nameHi: "गुलाब जामुन विथ आइसक्रीम",
        category: "desserts",
        price: 120,
        desc: "Warm syrup soaked mawa dumplings served alongside chilled vanilla cream.",
        prepTime: "5 Min",
        img: "assets/food_gulabjamun.jpg",
        isVeg: true
    },
    {
        id: "ds_3",
        name: "Royal Ice Cream Scoop",
        nameHi: "रॉयल आइसक्रीम स्कूप",
        category: "desserts",
        price: 80,
        desc: "Rich creamy scoops: Belgian Chocolate, Roasted Almond, or Vanilla.",
        prepTime: "5 Min",
        img: "assets/food_icecream.jpg",
        isVeg: true
    }
];
