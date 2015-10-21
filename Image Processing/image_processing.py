import os
from PIL import Image, ImageFilter

#IMAGE PROPERTIES
name = "testimage.jpeg"
folder = "assets"+"/"


"""
Function: Sharpen Image
args: path-Image
"""

def sharpen_img(path,img_name):
	img = Image.open(path+img_name)
	sharp_img = img.filter(ImageFilter.SHARPEN)
	sharp_img.save("sharp_"+img_name,'JPEG')


def exif():
	exifdata = im._getexif()
	print(exifdata)


sharpen_img(folder,name)
