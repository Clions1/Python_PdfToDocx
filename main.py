from pdf2docx import Converter

pdf_file="sample.pdf"
docx_path="outputfile.docx"

cv=Converter(pdf_file)
cv.convert(docx_path)
cv.close()