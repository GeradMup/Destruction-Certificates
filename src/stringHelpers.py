import os

def afterDelimeter(string, delimeter):
    splitedString = string.split(delimeter)
    pathString = splitedString[1]
    pathString = pathString.replace('\n','')
    return pathString

def filePath(titlePath, number=0):

    checkPath=""
    if number == 0:
        checkPath = titlePath + ".pdf"
    else:
        checkPath = titlePath + "_" + str(number) + ".pdf"
    
    
    if os.path.exists(checkPath):
        return filePath(titlePath, number + 1)
    
    else:
        return checkPath