import pyttsx3
import PyPDF3


book=open('first.pdf','rb')
pdfReader=PyPDF3.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()
page=pdfReader.getPage(3)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()
