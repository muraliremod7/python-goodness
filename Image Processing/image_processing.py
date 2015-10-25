from PIL import Image, ImageFilter

#IMAGE PROPERTIES
name = "testimage.jpeg"
folder = "assets"+"/"

#Open Image
#returns the Image object
def open_img(img_name):
	img = Image.open(img_name)
	return img

#Sharpen Image Function
def sharpen_img(path,img_name):
	img = open_img(img_name)
	sharp_img = img.filter(ImageFilter.SHARPEN)
	sharp_img.save("sharp_"+img_name,'JPEG')

#Resize Image Function
def resize_img(img_name,length,width):
	img = open_img(img_name)
	resized_img = img.resize((width,length))
	resized_img.save("resized_"+img_name,'JPEG')

#Get Image Exif Data
def exif(img_name):
	img = open_img(img_name)
	exifdata = img._getexif()
	print(exifdata)

#Rotate Image
def rotate_img(img_name,degrees):
	img = open_img(img_name)
	rotated_img = img.rotate(degrees)
	rotated_img.save("rotated_"+img_name,'JPEG')

#Test Functions
resize_img("testimage.jpeg",40,30) #resize test image to 40 by 30
rotate_img("testimage.jpeg",45) #rotate test image by 45 degrees counter-clockwise
