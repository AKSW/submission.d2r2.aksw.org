from pypdf import PdfWriter, PdfReader

import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def fill_text(agreement_pdf, output, data):

    corresponding_author = data["corresponding_author"]
    event = data["event"]

    form_text = io.BytesIO()
    can = canvas.Canvas(form_text, pagesize=A4)
    can.setFont('Courier', 12)
    can.drawString(20, 710, data["title"])
    can.drawString(20, 695, data["title_line2"])
    can.drawString(20, 650, data["authors"])
    can.drawString(70, 585, corresponding_author["name"])
    can.drawString(70, 563, corresponding_author["affiliation"])
    can.drawString(70, 539, corresponding_author["address"])
    can.drawString(70, 518, corresponding_author["email"])
    can.drawString(20, 420, event["title"])
    can.drawString(20, 405, event["title_line2"])
    can.drawString(20, 375, event["editors"])
    can.drawString(20, 360, event["editors_line2"])
    can.save()

    form_text.seek(0)

    form_text_obj = PdfReader(form_text)
    form_text_page = form_text_obj.pages[0]

    pdf_reader = PdfReader(agreement_pdf)
    pdf_writer = PdfWriter()

    # Watermark all the pages
    page = pdf_reader.pages[0]
    page.merge_page(form_text_page)
    pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

def wrap_title(title):
    title_line2 = ""
    if (len(title) > 96):
        # todo search for last space befor title[96], split at the position of this space
        pass
    return title, title_line2

if __name__ == '__main__':
    LINE_LIMIT = 76

    data = {
        "title": "Title Line 1",
        "title_line2": "Title Line 2",
        "authors": "All Authors",
        "corresponding_author": {
            "name": "Corresponding Author",
            "affiliation": "Affiliation of Corresponding Author",
            "address": "Address of Affiliation",
            "email": "email of Corresponding Author"
        },
        "event": {
            "title": "Second International Workshop on Linked Data-driven Resilience Research 2023",
            "title_line2": "",
            "editors": "Ricardo Usbeck, Sören Auer, Julia Holze, Sebastian Tramp, and Natanael Arndt",
            "editors_line2": ""
        }
    }

    fill_text(
        agreement_pdf='ceur-author-agreement-ccby-ntp.pdf',
        output='agreement_filled.pdf',
        data=data)
