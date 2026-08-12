from fileContent import getContentFromFile
from contentProcess import parseEmailHeader, getDmarcPolicy
from validation import checkDomainMismatch

def main():

    # assign the content of .eml file
    fileContent = getContentFromFile()

    # get dict of keys and data
    headerData = parseEmailHeader(fileContent)

    # check from and return domain against each other  
    domainCheck = checkDomainMismatch(headerData)

    # get dmarcPolicy
    dmarcPolicy = getDmarcPolicy(headerData['AuthenticationResults'])

    print(dmarcPolicy)

if __name__ == '__main__':
    main()