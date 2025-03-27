from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib import colors
from stringHelpers import *
from datetime import datetime


def pdfGen():
   # initializing variables with values 
    resourcesDir = "..\\resources\\"
    programPaths = resourcesDir + "paths.txt"

    pathsFile = open(programPaths, "r")
    
    paths = pathsFile.readlines()
    outputFolder = afterDelimeter(paths[0], "|")

    print(outputFolder)

    #Inputs
    logo = resourcesDir + "Logo.png"
    signature = resourcesDir + "Green Enviro Signature.jpeg"
    date = datetime.today().strftime('%d %B %Y')
    company = "Technologia Group"
    contactPerson = "Isak Van Wyk"
    email = "isak.vanwyk@technologiagroup.com"
    contact = "081 016 1876"
    dateOfCollection = input("Enter Collection Date:").strip()
    productDescription = input("Enter Product Description:").strip()
    quantity = input("Enter product quantity in pallets:").strip() + " Pallets"

    fileName = outputFolder + f'\\ {company} {date}'
    path = filePath(fileName)
    
    # creating a pdf object 
    pdf = canvas.Canvas(path) 
    
    # Add the LOGO first   
    pdf.drawImage(logo, x= 25, y= 690, width=540, height=120, mask=None) 

    # setting the title of the document 
    documentTitle = 'DS'
    pdf.setTitle(documentTitle) 
    
    # registering a external font in python 
    #pdfmetrics.registerFont( 
    #    TTFont('abc', 'SakBunderan.ttf') 
    #) 
    
    # creating the title by setting it's font  
    # and putting it on the canvas 
    title = 'Destruction Certificate'
    pdf.setFont('Times-Bold', 25) 
    pdf.drawCentredString(300, 635, title) 
    xPos = 50
    yPos = 570
    yOffset = 15

    specialLine(pdf, title="Date", description=date, x=xPos, y=yPos)
    specialLine(pdf, title="Company", description=company, x=xPos, y=yPos - yOffset)
    specialLine(pdf, title="Contact Person", description=contactPerson, x=xPos, y=yPos - 2*yOffset)
    specialLine(pdf, title="Email Address", description=email, x=xPos, y=yPos - 3*yOffset)
    specialLine(pdf, title="Contact Numbers", description=contact, x=xPos, y=yPos - 4*yOffset)

    textLines = [ 
        f'This is to certify that all products collected from your premises on {dateOfCollection}', 
        'have been completely scrapped and recycled.', 
    ] 

    fontSize = 13
    # textline and for loop 
    text = pdf.beginText(x=50, y=465) 
    text.setFont("Times-Roman", fontSize) 
    for line in textLines: 
        text.textLine(line) 
    pdf.drawText(text) 
    
    yPos = 405
    specialLine(pdf, title="Description of Products", description=productDescription, x=xPos, y=yPos)
    specialLine(pdf, title="Quantity", description=quantity, x=xPos, y=yPos - yOffset)

    #Disclaimer
    disclaimer = [ 
        "We certify that all the material has been recycled in accordance with our organization's secure", 
        "destruction policies and in an environmentally friendly manner. National, Provincial and Local",
        "Legislation have been upheld. If you have any queries, please do not hesitate to contact us." 
    ] 

    text = pdf.beginText(x=50, y=345)
    text.setFont('Times-Roman', fontSize)
    for line in disclaimer:
        text.textLine(line)
    pdf.drawText(text)

    #Add Signature
    pdf.drawImage(signature, x=xPos, y= 200, width=150, height=50, mask=None)
    
   
    pdf.setFont("Times-Bold", fontSize)             
    pdf.drawString(x=xPos, y=190, text=f"Operations Director                                                                           {date}")
    pdf.drawString(x=xPos, y=175, text="Nicholas Mupfumisi")

    # saving the pdf 
    pdf.save() 

    print("Certificate Generated!")
    return

#---------------------------------------------------------------------------------------------------------

def specialLine(pdfObject, title, description, x, y):
    fontSize = 13
    title = title + ":"
    pdfObject.setFont('Times-Bold', fontSize) 
    pdfObject.drawString(x, y, title) 
    pdfObject.setFont('Times-Roman', fontSize)
    textWidth = stringWidth(title, 'Times-Bold', fontSize) 
    x += textWidth + 3
    pdfObject.drawString(x, y, description)
    return

#---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    pdfGen()

