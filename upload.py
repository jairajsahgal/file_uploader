import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json
import pandas as pd
import qrcode

import time
def upload_file():
	Tk().withdraw()

	print("Please select your file")
	time.sleep(1)

	filelocation = askopenfilename()
	file_name=filelocation.split("/")[-1]
	print(file_name)

	files = {
	    'file': (file_name, open(filelocation, 'rb')),
	}

	response = requests.post('https://file.io/', files=files)
	data=json.loads(response.text)
	if data["success"]==True:
		print("One use hyperlink with your file -> ",data["link"]," copied to your clipboard")
		img=qrcode.make(data["link"])
		img.save(file_name.split(".")[0]+".png")
		df=pd.DataFrame([data["link"]])
		df.to_clipboard(index=False,header=False)
		print("Created QR code for link with name: "+file_name.split(".")[0]+".png")

	else:
		print("Error: \n Please check your network \n Possible uploading same file too many times\n Else:\n Server problem")