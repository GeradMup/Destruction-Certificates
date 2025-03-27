from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib import colors
from stringHelpers import *


def pdfGen():
   # initializing variables with values 
    resourcesDir = "..\\resources\\"
    programPaths = resourcesDir + "paths.txt"

    pathsFile = open(programPaths, "r")
    
    paths = pathsFile.readlines()
    outputFolder = afterDelimeter(paths[0], "|")

    #read all inputs here
    dateOfCollection = "21 February 2025"


    print(outputFolder)

    fileName = outputFolder + '\\sample.pdf'
    documentTitle = 'sample'
    title = 'Destruction Certificate'

    image = resourcesDir + "Logo.png"
    
    # creating a pdf object 
    pdf = canvas.Canvas(fileName) 
    
    # Add the LOGO first   
    pdf.drawImage(image, x= 25, y= 690, width=540, height=120, mask=None) 

    # setting the title of the document 
    pdf.setTitle(documentTitle) 
    
    # registering a external font in python 
    #pdfmetrics.registerFont( 
    #    TTFont('abc', 'SakBunderan.ttf') 
    #) 
    
    # creating the title by setting it's font  
    # and putting it on the canvas 
    pdf.setFont('Times-Bold', 25) 
    pdf.drawCentredString(300, 635, title) 
    xPos = 50
    yPos = 570
    yOffset = 15

    specialLine(pdf, title="Date", description="27 February 2025", x=xPos, y=yPos)
    specialLine(pdf, title="Company", description="Technologia Group", x=xPos, y=yPos - yOffset)
    specialLine(pdf, title="Contact Person", description="Isak Van Wyk", x=xPos, y=yPos - 2*yOffset)
    specialLine(pdf, title="Email Address", description="isak.vanwyk@technologiagroup.com", x=xPos, y=yPos - 3*yOffset)
    specialLine(pdf, title="Contact Numbers", description="081 016 1876", x=xPos, y=yPos - 4*yOffset)

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
    specialLine(pdf, title="Description of Products", description="DSTV TOP COVERS", x=xPos, y=yPos)
    specialLine(pdf, title="Quantity", description="3 Pallets", x=xPos, y=yPos - yOffset)
    

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


    


    # saving the pdf 
    pdf.save() 

    print("Certificate Generated!")
    return

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


if __name__ == "__main__":
    pdfGen()

