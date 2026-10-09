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
    font_title = get_font(58, bold=True)
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
        [(sx - pill_pad_x, 350 - pill_pad_y), (sx + sw + pill_pad_x, 350 + (s_bbox[3] - s_bbox[1]) + pill_pad_y)],
        radius=18,
        fill="#d91438",
        outline="#ff2a51",
        width=2
    )
    draw.text((sx, 350), s_text, fill="#ffffff", font=font_sub)

    # Divider Line
    draw.line([(width // 4, 415), (3 * width // 4, 415)], fill="#d4af37", width=2)

    # 5. Main Action Callout
    c_text = "SCAN TO VIEW MENU & ORDER FROM CAR"
    c_bbox = draw.textbbox((0, 0), c_text, font=font_callout)
    cx = (width - (c_bbox[2] - c_bbox[0])) // 2
    draw.text((cx, 440), c_text, fill="#ffffff", font=font_callout)

    c_hi = "अपनी कार से डिजिटल मेन्यू देखें और ऑर्डर करें"
    c_hi_bbox = draw.textbbox((0, 0), c_hi, font=font_hindi)
    chx = (width - (c_hi_bbox[2] - c_hi_bbox[0])) // 2
    draw.text((chx, 490), c_hi, fill="#fbe69b", font=font_hindi)

    # 6. Center QR Code Frame (Enlarged and crisp)
    qr_display_size = 620
    qr_resized = qr_menu_img.resize((qr_display_size, qr_display_size), Image.Resampling.LANCZOS)
    qrx = (width - qr_display_size) // 2
    qry = 550

    frame_pad = 26
    draw.rounded_rectangle(
        [(qrx - frame_pad, qry - frame_pad), (qrx + qr_display_size + frame_pad, qry + qr_display_size + frame_pad)],
        radius=30,
        fill="#ffffff",
        outline="#d4af37",
        width=7
    )
    canvas.paste(qr_resized, (qrx, qry), qr_resized)

    # 7. Payment Apps Supported Row
    pay_top = 1250
    pay_w = 880
    pay_h = 100
    px = (width - pay_w) // 2
    draw.rounded_rectangle(
        [(px, pay_top), (px + pay_w, pay_top + pay_h)],
        radius=18,
        fill="#1e060c",
        outline="#d4af37",
        width=2
    )
    pay_text1 = "PAY VIA ANY APP: PHONEPE • GPAY • PAYTM • WHATSAPP • CASH"
    p1_b = draw.textbbox((0, 0), pay_text1, font=get_font(21, bold=True))
    draw.text(((width - (p1_b[2] - p1_b[0])) // 2, pay_top + 18), pay_text1, fill="#fbe69b", font=get_font(21, bold=True))

    pay_text2 = "UPI ID: 9111789220@ybl  •  Helpline: 9111789220"
    p2_b = draw.textbbox((0, 0), pay_text2, font=get_font(18, bold=False))
    draw.text(((width - (p2_b[2] - p2_b[0])) // 2, pay_top + 55), pay_text2, fill="#ffffff", font=get_font(18, bold=False))

    # 8. Address & Contact Box
    addr_top = 1400
    draw.line([(width // 4, addr_top), (3 * width // 4, addr_top)], fill="#d4af37", width=2)

    a_text = "📍 Lotus Hut, The Drive In Cafe, Indore"
    ab = draw.textbbox((0, 0), a_text, font=get_font(28, bold=True))
    draw.text(((width - (ab[2] - ab[0])) // 2, addr_top + 30), a_text, fill="#fbe69b", font=get_font(28, bold=True))

    c_box_w = 780
    c_box_h = 90
    cbx = (width - c_box_w) // 2
    cby = addr_top + 85
    draw.rounded_rectangle(
        [(cbx, cby), (cbx + c_box_w, cby + c_box_h)],
        radius=18,
        fill="#d91438",
        outline="#ff2a51",
        width=3
    )
    c_call = "📞 CALL & WHATSAPP: +91 91117 89220"
    cc_b = draw.textbbox((0, 0), c_call, font=get_font(30, bold=True))
    draw.text(((width - (cc_b[2] - cc_b[0])) // 2, cby + 24), c_call, fill="#ffffff", font=get_font(30, bold=True))

    # Save
    canvas.convert("RGB").save(output_path, "PNG", quality=95)
    print("Luxury Standee saved:", output_path)

if __name__ == "__main__":
    menu_url = "https://hospitalityqr.github.io/shree-driving/?v=2"
    upi_url = "upi://pay?pa=9111789220@ybl&pn=Lotus%20Hut%20The%20Drive%20In%20Cafe&cu=INR"

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
