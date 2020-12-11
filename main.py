import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json
import pandas as pd
import requests
import time
from upload import upload_file
from get import get_file


choice=input(" To Upload File -> Enter U \n To Download File -> Enter D:\n Your Input-> ")
if(choice=="U" or choice=="u") and (len(choice)==1):
	upload_file()
elif(choice=="D" or choice=="d") and (len(choice)==1):
	get_file()
else:
	print("Wrong Input")
	exit(1)