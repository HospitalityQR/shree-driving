import os
import qrcode
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_font(size, bold=False, hindi=False):
    if hindi:
        candidates = ["Nirmala.ttc", "mangal.ttf", "aparaj.ttf"]
        for name in candidates:
            p = os.path.join("C:\\Windows\\Fonts", name)
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size)
                except Exception:
                    pass
    candidates = []
    if bold:
        candidates = ["arialbd.ttf", "segoeuib.ttf", "georgiab.ttf"]
    else:
        candidates = ["arial.ttf", "segoeui.ttf", "georgia.ttf"]

    for name in candidates:
        p = os.path.join("C:\\Windows\\Fonts", name)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def generate_styled_qr(data_url, logo_path="logo.png", size=600):
    """Generate high-resolution QR with embedded center logo."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=3,
    )
    qr.add_data(data_url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="#120406", back_color="#ffffff").convert("RGBA")
    qr_img = qr_img.resize((size, size), Image.Resampling.LANCZOS)

    # Embed center logo if available
    if os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo_box_size = int(size * 0.26)
            logo = logo.resize((logo_box_size, logo_box_size), Image.Resampling.LANCZOS)

            # Circular mask for logo
            mask = Image.new("L", (logo_box_size, logo_box_size), 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.ellipse((0, 0, logo_box_size, logo_box_size), fill=255)

            # Background circle with gold rim
            bg_pad = 8
            bg_circle_size = logo_box_size + bg_pad * 2
            bg_circle = Image.new("RGBA", (bg_circle_size, bg_circle_size), (0, 0, 0, 0))
            draw_bg = ImageDraw.Draw(bg_circle)
            draw_bg.ellipse((0, 0, bg_circle_size, bg_circle_size), fill="#ffffff", outline="#d4af37", width=4)

            pos_x = (size - bg_circle_size) // 2
            pos_y = (size - bg_circle_size) // 2
            qr_img.paste(bg_circle, (pos_x, pos_y), bg_circle)

            logo_pos_x = (size - logo_box_size) // 2
            logo_pos_y = (size - logo_box_size) // 2
            qr_img.paste(logo, (logo_pos_x, logo_pos_y), mask)
        except Exception as e:
            print("Logo embed notice:", e)

    return qr_img

def build_luxury_standee(qr_menu_img, width=1200, height=1800, output_path="table_standee_printable.png"):
    """Render 300DPI luxury printable standee."""
    # 1. Base Dark Crimson Ambient Canvas
    canvas = Image.new("RGBA", (width, height), "#0a0204")

    # If night ambience photo exists, crop off phone status/comment bar and blend
    if os.path.exists("ambience_night.png"):
        try:
            amb = Image.open("ambience_night.png").convert("RGBA")
            # crop bottom 8% if needed to remove 'Add comment' bar
            aw, ah = amb.size
            amb = amb.crop((0, 0, aw, int(ah * 0.90)))
            amb = amb.resize((width, height), Image.Resampling.LANCZOS)
            # Dark luxury overlay
            overlay = Image.new("RGBA", (width, height), (10, 2, 4, 218))
            amb = Image.alpha_composite(amb, overlay)
            canvas = amb
        except Exception:
            pass

    draw = ImageDraw.Draw(canvas)

    # 2. Luxury Gold Borders & Corner Accents
    gold_border_outer = 24
    gold_border_inner = 36
    draw.rectangle(
        [(gold_border_outer, gold_border_outer), (width - gold_border_outer, height - gold_border_outer)],
        outline="#d4af37",
        width=5
    )
    draw.rectangle(
        [(gold_border_inner, gold_border_inner), (width - gold_border_inner, height - gold_border_inner)],
        outline="#fbe69b",
        width=2
    )

    # Corner brackets
    for cx, cy in [(gold_border_inner, gold_border_inner), (width - gold_border_inner, gold_border_inner),
                   (gold_border_inner, height - gold_border_inner), (width - gold_border_inner, height - gold_border_inner)]:
        draw.rectangle([(cx - 5, cy - 5), (cx + 5, cy + 5)], fill="#d4af37")

    # 3. Logo at Top
    if os.path.exists("logo.png"):
        try:
            logo = Image.open("logo.png").convert("RGBA")
            logo_size = 170
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            mask = Image.new("L", (logo_size, logo_size), 0)
            ImageDraw.Draw(mask).ellipse((0, 0, logo_size, logo_size), fill=255)
            
            lx = (width - logo_size) // 2
            ly = 85
            
            draw.ellipse([(lx - 6, ly - 6), (lx + logo_size + 6, ly + logo_size + 6)], fill="#ffffff", outline="#d4af37", width=5)
            canvas.paste(logo, (lx, ly), mask)
        except Exception as e:
            print("Logo error:", e)

    # 4. Brand Typography
    font_title = get_font(56, bold=True)
    font_sub = get_font(26, bold=True)
    font_callout = get_font(34, bold=True)
    font_hindi = get_font(26, bold=True, hindi=True)

    # "LOTUS HUT"
    t_text = "LOTUS HUT"
    t_bbox = draw.textbbox((0, 0), t_text, font=font_title)
    tx = (width - (t_bbox[2] - t_bbox[0])) // 2
    draw.text((tx, 275), t_text, fill="#fbe69b", font=font_title)

    # "THE DRIVE IN CAFE" Pill
    s_text = "THE DRIVE IN CAFE"
    s_bbox = draw.textbbox((0, 0), s_text, font=font_sub)
    sw = s_bbox[2] - s_bbox[0]
    sx = (width - sw) // 2
    pill_pad_x = 24
    pill_pad_y = 8
    draw.rounded_rectangle(
        [(sx - pill_pad_x, 345 - pill_pad_y), (sx + sw + pill_pad_x, 345 + (s_bbox[3] - s_bbox[1]) + pill_pad_y)],
        radius=18,
        fill="#d91438",
        outline="#ff2a51",
        width=2
    )
    draw.text((sx, 345), s_text, fill="#ffffff", font=font_sub)

    # Tagline
    tag_text = "CAR PARKING SERVICE  •  GOURMET COFFEE  •  FAST BITES"
    tag_bbox = draw.textbbox((0, 0), tag_text, font=get_font(20, bold=True))
    tag_x = (width - (tag_bbox[2] - tag_bbox[0])) // 2
    draw.text((tag_x, 405), tag_text, fill="#e8c7cf", font=get_font(20, bold=True))

    # Divider Line
    draw.line([(width // 4, 445), (3 * width // 4, 445)], fill="#d4af37", width=2)

    # 5. Main Action Callout
    c_text = "SCAN FROM YOUR CAR TO ORDER"
    c_bbox = draw.textbbox((0, 0), c_text, font=font_callout)
    cx = (width - (c_bbox[2] - c_bbox[0])) // 2
    draw.text((cx, 470), c_text, fill="#ffffff", font=font_callout)

    c_hi = "अपनी कार से सीधे डिजिटल मेन्यू ऑर्डर करें"
    c_hi_bbox = draw.textbbox((0, 0), c_hi, font=font_hindi)
    chx = (width - (c_hi_bbox[2] - c_hi_bbox[0])) // 2
    draw.text((chx, 520), c_hi, fill="#fbe69b", font=font_hindi)

    # 6. Center QR Code Frame
    qr_display_size = 560
    qr_resized = qr_menu_img.resize((qr_display_size, qr_display_size), Image.Resampling.LANCZOS)
    qrx = (width - qr_display_size) // 2
    qry = 580

    frame_pad = 22
    draw.rounded_rectangle(
        [(qrx - frame_pad, qry - frame_pad), (qrx + qr_display_size + frame_pad, qry + qr_display_size + frame_pad)],
        radius=26,
        fill="#ffffff",
        outline="#d4af37",
        width=6
    )
    canvas.paste(qr_resized, (qrx, qry), qr_resized)

    # 7. UPI Payment Highlight Card
    upi_card_top = 1210
    upi_card_w = 820
    upi_card_h = 175
    ucx = (width - upi_card_w) // 2
    draw.rounded_rectangle(
        [(ucx, upi_card_top), (ucx + upi_card_w, upi_card_top + upi_card_h)],
        radius=20,
        fill="#1e060c",
        outline="#d4af37",
        width=3
    )

    upi_label = "INSTANT UPI PAYMENT (GPAY / PHONEPE / PAYTM)"
    draw.text((ucx + 35, upi_card_top + 18), upi_label, fill="#fbe69b", font=get_font(21, bold=True))

    upi_num = "PAY DIRECTLY TO: 9111789220"
    draw.text((ucx + 35, upi_card_top + 54), upi_num, fill="#ffffff", font=get_font(34, bold=True))

    upi_sub = "UPI ID: 9111789220@upi  •  Cash Accepted at Car Delivery"
    draw.text((ucx + 35, upi_card_top + 110), upi_sub, fill="#d6b8be", font=get_font(20, bold=False))

    # 8. Steps Row
    steps_y = 1420
    steps = [
        "1. Scan QR",
        "2. Add Car No.",
        "3. WhatsApp Order",
        "4. Served at Car"
    ]
    step_w = width // len(steps)
    for i, s in enumerate(steps):
        sx = i * step_w + 10
        draw.rounded_rectangle(
            [(sx + 10, steps_y), (sx + step_w - 20, steps_y + 60)],
            radius=12,
            fill="#2c0912",
            outline="#fbe69b",
            width=1
        )
        sb = draw.textbbox((0, 0), s, font=get_font(18, bold=True))
        stx = sx + 10 + (step_w - 30 - (sb[2] - sb[0])) // 2
        draw.text((stx, steps_y + 18), s, fill="#ffffff", font=get_font(18, bold=True))

    # 9. Footer Info
    foot_y = 1520
    draw.line([(width // 4, foot_y), (3 * width // 4, foot_y)], fill="#d4af37", width=1)

    f_text1 = "LOTUS HUT  •  THE DRIVE IN CAFE  •  INDORE"
    f1_b = draw.textbbox((0, 0), f_text1, font=get_font(22, bold=True))
    draw.text(((width - (f1_b[2] - f1_b[0])) // 2, foot_y + 20), f_text1, fill="#fbe69b", font=get_font(22, bold=True))

    f_text2 = "Direct Helpline & Service Staff: +91 91117 89220"
    f2_b = draw.textbbox((0, 0), f_text2, font=get_font(26, bold=True))
    draw.text(((width - (f2_b[2] - f2_b[0])) // 2, foot_y + 60), f_text2, fill="#ffffff", font=get_font(26, bold=True))

    f_text3 = "Fresh Preparation Time: 15-20 Min  •  Pure Quality Ingredients"
    f3_b = draw.textbbox((0, 0), f_text3, font=get_font(18, bold=False))
    draw.text(((width - (f3_b[2] - f3_b[0])) // 2, foot_y + 110), f_text3, fill="#c9a4ac", font=get_font(18, bold=False))

    # Save
    canvas.convert("RGB").save(output_path, "PNG", quality=95)
    print("Luxury Standee saved:", output_path)

if __name__ == "__main__":
    menu_url = "https://hospitalityqr.github.io/shree-driving/?v=2"
    upi_url = "upi://pay?pa=9111789220@upi&pn=Lotus%20Hut%20The%20Drive%20In%20Cafe&cu=INR"

    print("Generating Menu QR...")
    qr_menu = generate_styled_qr(menu_url, logo_path="logo.png", size=800)
    qr_menu.save("qr_digital_menu.png")
    qr_menu.save("qr_code.png")

    print("Generating UPI QR...")
    qr_upi = generate_styled_qr(upi_url, logo_path="logo.png", size=800)
    qr_upi.save("qr_payment_upi.png")

    print("Generating 300 DPI Luxury Printable Standees...")
    build_luxury_standee(qr_menu, output_path="table_standee_printable.png")
    build_luxury_standee(qr_menu, output_path="car_standee_printable.png")
    print("Done!")
