from PyPDF2 import PdfFileReader, PdfFileWriter

# the patient's file is opened based on the name (last name, first name)
patient_name = input("Enter the patient's name: ")
pdf_name = patient_name + '.pdf'

# opening the file and creating a reader and writer
pdf = open('/Users/niyas/Desktop/scan folder/{}'.format(pdf_name), 'rb')
pdf_reader = PdfFileReader(pdf)
pdf_writer = PdfFileWriter()

# getting the first two pages of the pdf (pet scan report) and creating a separate file
pdf_writer.addPage(pdf_reader.getPage(0))
pdf_writer.addPage(pdf_reader.getPage(1))
pet_name = patient_name + ' pet'
pet_scan = open('/Users/niyas/Desktop/{}'.format(pet_name), 'wb')
pdf_writer.write(pet_scan)
pdf.close()

# opening the file again and creating a reader and writer
pdf = open('/Users/niyas/Desktop/scan folder/{}'.format(pdf_name), 'rb')
pdf_reader = PdfFileReader(pdf)
pdf_writer = PdfFileWriter()

# getting the next two pages of the pdf (insurance pictures) and creating a separate file
pdf_writer.addPage(pdf_reader.getPage(2))
pdf_writer.addPage(pdf_reader.getPage(3))
ins_name = patient_name + ' ins'
ins_card = open('/Users/niyas/Desktop/{}'.format(ins_name), 'wb')
pdf_writer.write(ins_card)
pdf.close()

# opening the file again and creating a reader and writer
pdf = open('/Users/niyas/Desktop/scan folder/{}'.format(pdf_name), 'rb')
pdf_reader = PdfFileReader(pdf)
pdf_writer = PdfFileWriter()

# getting the next page of the pdf (authorization) and creating a separate file
pdf_writer.addPage(pdf_reader.getPage(4))
auth_name = patient_name + ' auth'
auth_form = open('/Users/niyas/Desktop/{}'.format(auth_name), 'wb')
pdf_writer.write(auth_form)
pdf.close()

# opening the file again and creating a reader and writer
pdf = open('/Users/niyas/Desktop/scan folder/{}'.format(pdf_name), 'rb')
pdf_reader = PdfFileReader(pdf)
pdf_writer = PdfFileWriter()

# getting the next page of the pdf (hippa) and creating a separate file
pdf_writer.addPage(pdf_reader.getPage(5))
hippa_name = patient_name + ' hippa'
hippa_form = open('/Users/niyas/Desktop/{}'.format(hippa_name), 'wb')
pdf_writer.write(hippa_form)
pdf.close()