from PyPDF2 import PdfFileMerger
pdfs = ['exp-1.pdf','exp-5.pdf', 'exp-6.pdf', 'exp-7.pdf', 'exp-8_9.pdf','exp-10.pdf']

merger = PdfFileMerger(strict= False)

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()