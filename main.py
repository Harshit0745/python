from pypdf import PdfWriter
merger=PdfWriter()
pdfs=["discreate_maths.pdf","VB_NET.pdf"]
for pdf in pdfs:
    merger.append(pdf)
merger.write("merged.pdf")
