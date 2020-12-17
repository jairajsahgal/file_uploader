# Description
Upload your file and get link.

# Requirements
* python3
* requests==2.25.0
* pandas==1.1.5

# How to setup program
```bash
pip install -r requirements.txt
python main.py
```
# How to use program

[Program working](https://github.com/jairajsahgal/file_uploader/main/simplescreenrecorder-2020-12-12_21.59.29.gif)

# Working
The project uses python programming language, Using tkinter library, it gets the location of the file using GUI.
Then using requests library, it uploads the file and the name of the file. Using POST method, uploads the file on https://www.file.io/ website, which returns one time use hyperlink of the file.
The project also includes another function that can retrieve the file using the hyperlink of the file though the user has to enter the extension of the file.


# Future Enhancements
* Multiple File Support.
* Automatic Extension Recognition.
* More GUI for non-command line people.
* Voice Assistance.
