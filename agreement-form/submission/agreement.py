from pypdf import PdfWriter, PdfReader

import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import yaml
import click

LINE_LIMIT = 76


def split_line(line):
    if len(line) > LINE_LIMIT:
        split_pos = line[:LINE_LIMIT].rfind(' ')
        if len(line[split_pos + 1:]) > LINE_LIMIT:
            second_line = split_line(line[split_pos + 1:])
            return line[:split_pos], second_line[0], second_line[1]
        return line[:split_pos], line[split_pos + 1:], ""
    return line, "", ""


def fill_text(agreement_pdf, output, data, editor):

    corresponding_author = data["corresponding_author"]
    event = data["event"]

    form_text = io.BytesIO()
    can = canvas.Canvas(form_text, pagesize=A4)
    can.setFont('Courier', 12)
    if editor:
        editor_shift = 37
        can.drawString(20, 686, split_line(event["title"])[0])
        can.drawString(20, 671, split_line(event["title"])[1])
        can.drawString(20, 628, split_line(event["editors"])[0])
        can.drawString(20, 601, split_line(event["editors"])[1])
        can.drawString(70, 586 - editor_shift, event["corresponding_editor"]["name"])
        can.drawString(70, 563 - editor_shift, split_line(event["corresponding_editor"]["affiliation"])[0])
        can.drawString(70, 553 - editor_shift, split_line(event["corresponding_editor"]["affiliation"])[1])
        can.drawString(70, 540 - editor_shift, split_line(event["corresponding_editor"]["address"])[0])
        can.drawString(70, 530 - editor_shift, split_line(event["corresponding_editor"]["address"])[1])
        can.drawString(70, 517 - editor_shift, event["corresponding_editor"]["email"])
    else:
        can.drawString(20, 710, split_line(data["title"])[0])
        can.drawString(20, 695, split_line(data["title"])[1])
        can.drawString(20, 680, split_line(data["title"])[2])
        can.drawString(20, 653, split_line(data["authors"])[0])
        can.drawString(20, 638, split_line(data["authors"])[1])
        can.drawString(20, 623, split_line(data["authors"])[2])
        can.drawString(70, 586, corresponding_author["name"])
        can.drawString(70, 563, split_line(corresponding_author["affiliation"])[0])
        can.drawString(70, 553, split_line(corresponding_author["affiliation"])[1])
        can.drawString(70, 540, split_line(corresponding_author["address"])[0])
        can.drawString(70, 530, split_line(corresponding_author["address"])[1])
        can.drawString(70, 517, corresponding_author["email"])
        can.drawString(20, 420, split_line(event["title"])[0])
        can.drawString(20, 405, split_line(event["title"])[1])
        can.drawString(20, 375, split_line(event["editors"])[0])
        can.drawString(20, 360, split_line(event["editors"])[1])
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


@click.command()
@click.option("--metadata", default="metadata.yml", help="The metadata.yml file.")
@click.option("--template", default="ceur-author-agreement-ccby-ntp.pdf", help="The template pdf file.")
@click.option("--output", default="agreement_filled.pdf", help="The filled pdf file.")
@click.option("--editor", help="If an editor form is filled.", is_flag=True)
def fill_form(metadata, template, output, editor):
    """Fill the form with the metadata provided."""
    with open(metadata, "r") as stream:
        try:
            data = yaml.safe_load(stream)
            print(data)
        except yaml.YAMLError as exc:
            print(exc)

    for paper in data.values():
        paper["authors"] = ", ".join([author["name"] for author in paper["authors"]])
        fill_text(agreement_pdf=template, output=output, data=paper, editor=editor)


if __name__ == '__main__':
    fill_form()
