def afterDelimeter(string, delimeter):
    splitedString = string.split(delimeter)
    pathString = splitedString[1]
    pathString = pathString.replace('\n','')
    return pathString