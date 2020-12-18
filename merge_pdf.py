from PyPDF2 import PdfFileMerger
pdfs = ['merge\exp-1.pdf','merge\exp-5.pdf', 'merge\exp-6.pdf', 'merge\exp-7.pdf', 'merge\exp-8_9.pdf','merge\exp-10.pdf']

merger = PdfFileMerger(strict= False)

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()