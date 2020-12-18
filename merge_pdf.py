import os
from PyPDF2 import PdfFileMerger


dir_path = os.path.dirname(os.path.realpath('merge'))

dir_path=dir_path+'\\merge'
print(dir_path)

#pdfs = ['merge\exp-1.pdf','merge\exp-5.pdf', 'merge\exp-6.pdf', 'merge\exp-7.pdf', 'merge\exp-8_9.pdf','merge\exp-10.pdf']

#path= r'C:\Users\hp\Desktop\pdf_reader\merge'

pdfs=[a for a in os.listdir(dir_path) if a.endswith(".pdf")]
print(pdfs)
merger = PdfFileMerger(strict= False)

for pdf in pdfs:
    
    path=dir_path+"\\"+ pdf
    print(path)
    merger.append(open(path,'rb'))

with open("result.pdf", "wb") as fout:
    merger.write("result.pdf")
merger.close()

