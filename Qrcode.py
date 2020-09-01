import pyqrcode #pip install pyqrcode
import png #pip install png
from pyqrcode import QRCode

QRstring = input("website :")  #paste any URL
url = pyqrcode.create(QRstring)

directory = (input("Path to save the file :")) #path to save the file
#format for eg:--- D:\path or C:\path
file_name = input("file name: ") #name of the file to be written with .png extension
url.png(directory + file_name, scale = 8)
