import os
from PyPDF2 import PdfFileReader, PdfFileWriter

for root, dirs, files in os.walk('/Users/niyas/Desktop/scanning'):
    for file_name in files:
        if '.pdf' in file_name:
            pdf = open('/Users/niyas/Desktop/scanning/{}'.format(file_name), 'rb')

            # getting the first two pages of the pdf (pet scan report) and creating a separate file
            pdf_reader = PdfFileReader(pdf)
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(0))
            pdf_writer.addPage(pdf_reader.getPage(1))
            pet_name = file_name + ' pet'
            pet_scan = open('/Users/niyas/Desktop/{}'.format(pet_name), 'wb')
            pdf_writer.write(pet_scan)

            # getting the next two pages of the pdf (insurance info) and creating a separate file
            pdf_reader = PdfFileReader(pdf)
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(2))
            pdf_writer.addPage(pdf_reader.getPage(3))
            ins_name = file_name + ' ins'
            ins_card = open('/Users/niyas/Desktop/{}'.format(ins_name), 'wb')
            pdf_writer.write(ins_card)
            pdf.close()