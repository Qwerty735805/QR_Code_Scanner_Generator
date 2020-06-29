import qrcode

# Create qr code instance
QR = qrcode.QRCode()

# The data that you want to convert
data = "https://tantrabyte.org/"


# Add data
QR.add_data(data)
QR.make(fit=True)

# Create an image from the QR Code instance
img = QR.make_image()

img.save("image.png")