# pip install fpdf2
from fpdf import FPDF
pdf = FPDF()

imagelist = []

for image in imagelist:
    pdf.add_page()
    pdf.image(image, x = 10, y = 10, w = 100)

pdf.output("yourfile.pdf")