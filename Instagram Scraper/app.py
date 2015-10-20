from flask import Flask,render_template,request 
import requests
import urllib.request
from bs4 import BeautifulSoup
import json
import os
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST' and 'iurl' in request.form:
		url=request.form['iurl']
		raw=requests.get(url)
		soup=BeautifulSoup(raw.text,'html.parser')

		data= soup.find_all('script')[5].contents
		info=data[0]
		json_data=json.loads(info[21:-1])

		final_data=json_data['entry_data']['PostPage']
		final=final_data[0]
		image=final['media']['display_src']

		while image!='':
			print(image)
			download_photo(image, "1.jpg")
			print("image saved")
			return "<img src="+image+" align='center'>"
			
			return render_template('index.html')


def download_photo(img_url, filename):
        image_on_web = urllib.urlopen(img_url)
        if image_on_web.headers.maintype == 'image':
            buf = image_on_web.read()
            path = os.getcwd() + "/img"
            file_path = "%s%s" % (path, filename)
            downloaded_image = file(file_path, "wb")
            downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
        else:
            return False    


if __name__=='__main__':
	app.run()