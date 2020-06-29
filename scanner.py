import cv2
detector = cv2.QRCodeDetector()

#Path of the QR code image.
img_path="image.png"
img = cv2.imread(img_path)
data, bbox, temp = detector.detectAndDecode(img)

if data:
    print("QR Code detected, data:    ", data)
else:
	print("No QR Code Detected")