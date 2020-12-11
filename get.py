import requests

def get_file():
	link=input("Enter uploaded link: ")
	if "file" in link:
		response = requests.get(link)
		content=response.text
		extension=input("Enter extension of file like txt, pptx, mp3: ")
		with open("new."+extension,"w") as file_object:
			file_object.write(content)
		print("File saved as : "+"new."+extension)
	else:
		print("Error: Possible reasons\n Link not from file.io\n")
		print("Internet not working")
		print("No link passed")
