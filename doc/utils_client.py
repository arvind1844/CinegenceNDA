# # importing the necessary libraries
# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa  

# # defining the function to convert an HTML file to a PDF file
# def html_to_pdf(template_src, context_dict={}):
#      template = get_template(template_src)
#      html  = template.render(context_dict)
#      result = BytesIO()
#      pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#      if not pdf.err:
#          return HttpResponse(result.getvalue(), content_type='application/pdf')
#      return None

def pdf2(nda_client):
    from borb.pdf.document.document import Document
    from borb.pdf.canvas.layout.table.flexible_column_width_table import (
    FlexibleColumnWidthTable,
)
    from borb.pdf.page.page import Page
    from borb.pdf.pdf import PDF
    from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
    from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
   

    # Create empty Document
    pdf = Document()

    # Create empty Page
    page = Page()

    # Add Page to Document
    pdf.add_page(page)

    # Create PageLayout
    layout: PageLayout = SingleColumnLayout(page)
    # New import(s)
    from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
    from borb.pdf.canvas.layout.text.paragraph import Paragraph
    from borb.pdf.canvas.layout.forms.text_field import TextField
    from borb.pdf.canvas.color.color import HexColor
    from decimal import Decimal
    from borb.pdf.canvas.layout.layout_element import Alignment
    from borb.pdf.canvas.layout.forms.drop_down_list import DropDownList
    from borb.pdf.canvas.geometry.rectangle import Rectangle
    
    
    

    # Let's start by adding a heading
    layout.add(Paragraph("Client Information:",horizontal_alignment=Alignment.CENTERED, font="Helvetica-Bold"))
    layout.add(Paragraph("Data Protection Policy", 
                        font="Helvetica-Bold",horizontal_alignment=Alignment.CENTERED,))
    # r: Rectangle = Rectangle(
    #     Decimal(59),                # x: 0 + page_margin
    #     Decimal(848 - 84),    # y: page_height - page_margin - height_of_textbox
    #     Decimal(595 - 59 * 2),      # width: page_width - 2 * page_margin
    #     Decimal(200),               # height
    # )
    # Dummy text
    layout.add(Paragraph(
        """
        ** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        ** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """,
            
              font="Helvetica", text_alignment=Alignment.JUSTIFIED,
    ))
    m: Decimal = Decimal(60)
    layout.add(Paragraph( 
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""",
        font="Helvetica", 
        text_alignment=Alignment.JUSTIFIED, margin_bottom=m,))
    
    
    layout.add(
        FlexibleColumnWidthTable(number_of_columns=2, number_of_rows=4)
        .add(Paragraph("Name:"))
        .add(Paragraph(str(nda_client.name)))
        .add(Paragraph("Email:"))
        .add(Paragraph(str(nda_client.email)))       
        .add(Paragraph("Aadhar Number:"))
        .add(Paragraph(str(nda_client.aadhar)))
        .add(Paragraph("PAN Number:"))
        .add(Paragraph(str(nda_client.pan_number)))
           
        .set_padding_on_all_cells(Decimal(6), Decimal(10),Decimal(5), Decimal(5),)
        .no_borders(),
    )
    layout.add(Paragraph("Stephen Mascarenhas,",horizontal_alignment=Alignment.RIGHT, font="Helvetica-Bold"))
    layout.add(Paragraph("CEO and Founder",horizontal_alignment=Alignment.RIGHT, font="Helvetica-Bold"))
    
    from borb.pdf.canvas.layout.image.image import Image
        
    layout.add(Image(
                    "http://127.0.0.1:8000"+str(nda_client.image.url),
                    width=Decimal(128),
                    height=Decimal(128),
                ),
                
    )
    # New import(s)
    import typing
    from borb.pdf.canvas.geometry.rectangle import Rectangle
    from borb.pdf.page.page_size import PageSize
    from borb.pdf.canvas.line_art.line_art_factory import LineArtFactory
    # from borb.pdf.canvas.layout.shape.shape  import Shape

    ps: typing.Tuple[Decimal, Decimal] = PageSize.A4_PORTRAIT.value
    r: Rectangle = Rectangle(Decimal(0), Decimal(32), ps[0], Decimal(8))
    # Shape(points=LineArtFactory.rectangle(r), stroke_color=HexColor("56cbf9"), fill_color=HexColor("56cbf9")).layout(page, r)
    # New import(s)
    from borb.pdf.pdf import PDF

    # Store
    with open("template/client.pdf", "wb") as out_file_handle:
        PDF.dumps(out_file_handle, pdf)

    import subprocess
    subprocess.Popen(["C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe", "template/client.pdf"])