import pyqrcode
import png
from pyqrcode import QRCode

QRstring = input("website :")  #paste any URL
url = pyqrcode.create(QRstring)

directory = (input("Path to save the file :")) #path to save the file
#format for eg:--- D:\filename or C:\filename
file_name = input("file name: ")
url.png(directory + file_name, scale = 8)
