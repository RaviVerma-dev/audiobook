import pyttsx3
import PyPDF2
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


# book = open('audiobook/oop.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages

# speaker = pyttsx3.init()
# for num in range(1, pages):
#     page = pdfReader.getPage(num)
#     text = page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()