import os
from PIL import Image, ImageFilter

#IMAGE PROPERTIES
name = "testimage.jpeg"
folder = "assets"+"/"


#Sharepn Image Function
def sharpen_img(path,img_name):
	img = Image.open(path+img_name)
	sharp_img = img.filter(ImageFilter.SHARPEN)
	sharp_img.save("sharp_"+img_name,'JPEG')

#Resize Image Function
def resize_img(img_name,length,width):
	img = Image.open(img_name)
	resized_img = img.resize((width,length))
	resized_img.save("resized_"+img_name,'JPEG')

def exif():
	exifdata = im._getexif()
	print(exifdata)


#Run Functions
resize_img("testimage.jpeg",650,500)
