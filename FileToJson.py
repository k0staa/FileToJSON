jsonFields = ["date_created", "date_sended", "image_location", "campaign_name", "user_id", "image_id", "shop_id", "shop_location", "image_path"]
fileName = 'PentaImage.log'

def isBlank (myString):
    return not (myString and myString.strip())

def writeToFile(json, outputFileName):
    outputFile = open(outputFileName, 'w')
    outputFile.write(json)

def createJSONfromFile(fileName):
    f = open(fileName, 'r')
    json = ""
    lineIndex = 5
    for line in f:
        lineIndex +=1
        tokenIndex = 0
        json += "PUT /attr/image/" + str(lineIndex) + ' { '
        for token in line.split('"'):
            print token
            print tokenIndex
            if (not isBlank(token)):
                json += ' "' + jsonFields[tokenIndex] + ' " : "' + token + '", '
                tokenIndex += 1
        json += ' } \n'
    return json

writeToFile(createJSONfromFile(fileName),'output')
