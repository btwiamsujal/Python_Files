import qrcode
from PIL import Image, ImageDraw
import time
import os


qr = qrcode.QRCode(
    version=5, 
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,  
    border=4,  
)


qr.add_data("https://github.com/btwiamsujal")
qr.make(fit=True)

qr_img = qr.make_image(fill_color="blue", back_color="white").convert("RGB")

mask = Image.new("L", qr_img.size, 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle([(0, 0), qr_img.size], radius=20, fill=255)
qr_img.putalpha(mask)

# qr_img.save("Fancy_Qr_code.png")

qr.print_ascii()

for remaining in range(60, 0, -1):
    print(f"\rTime remaining: {remaining} seconds", end="", flush=True)
    time.sleep(1)

print("\rTime's up!                      ")
