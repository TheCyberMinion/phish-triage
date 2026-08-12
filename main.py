from fileContent import getContentFromFile
from contentProcess import parseEmailHeader
from validation import checkDomainMismatch

def main():

    # assign the content of .eml file
    fileContent = getContentFromFile()

    # get dict of from, subject, return-path
    headerData = parseEmailHeader(fileContent)

    # check from and return domain against each other  
    domainCheck = checkDomainMismatch(headerData)

    print(domainCheck)

if __name__ == '__main__':
    main()