## QR_Code_Scanner_Generator

# scanner 

change the image path to where the qrcode image is saved(prefered png format).
Then run the file, the code decodes the QRcode
and displays(output) the data.

-----------------------------------------------------------

# QRcode_Generator

This file generates a QRcode for any given data.
Change the data variable, with the information u want to convert.

after running the file , the qrcode is saved in an png format.

----------------------------------------------------------

# webcamQRscanner

This tool is made using opencv python

OpenCV is used beacuse, it is popular and easy to integrate with the webcam or any video.

OpenCV already got QR code detector

detectAndDecode() function takes an image as an input and decodes it to return a tuple of 3 values:
1)the data decoded from the QR code,
2)the output array of vertices of the found QR code quadrangle ,
3)the output image containing rectified,binarized QR code.

cv2.line() function draws a line segment connecting two points, we retrieve these points from bbox array that was decoded by detectAndDecode() previously.
I had specified a red color ( (0, 0, 255) is red as OpenCV uses BGR colors ) and thickness of 2

Run this file 
and place any QR code in front of the webcam.
It decodes the code and give the output.


Click "q" to stop running the program. 
