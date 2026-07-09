import pyqrcode
from pyqrcode import QRCode

s = "https://www.geeksforgreeks.org"

url = pyqrcode.create(s)

url.png("myqr.png", scale = 6)
