import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
data = input()
qr.add_data(data)
qr.make(fit=True)

qr_image = qr.make_image(fill_color="black", back_color="white")

qr_image.save("qrcode.png")
print("QR code saved as qrcode.png")
