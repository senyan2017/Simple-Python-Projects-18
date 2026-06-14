#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import qrcode


def main():
    data = input("Enter the data to encode (or press Enter for default): ").strip()
    if not data:
        data = "https://github.com/Armin-Abdollahi"

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="White")

    img.save("qrcode.png")
    print(f"QR code saved as qrcode.png (data: {data})")


if __name__ == "__main__":
    main()
