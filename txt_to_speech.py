from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS
Tk().withdraw()  # close the tkinter window
filelocation = askopenfilename(initialdir = "/desktop/pdf_reader",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
with open(filelocation,'rb') as of:
    pdf=PyPDF2.PdfFileReader(of)
    page_number=0
    txt=''
    while page_number<pdf.getNumPages(): # gives tot
        page_data=pdf.getPage(page_number)
        txt+=page_data.extractText()
        page_number+=1
print(txt)
final_file = gTTS(text=txt, lang='en') 
final_file.save("Generated_Speech.mp3")  # save file to computer
print("Task Completed!!")



