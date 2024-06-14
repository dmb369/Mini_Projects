#QR stands for Quick Response which is a machine-readable label or code which contains the information.
#Pillow or PIL is a library in Python which is used to image class within it to show the image.

import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=sv5IibfIPU4")
img.save("Smruti_26.jpg")

