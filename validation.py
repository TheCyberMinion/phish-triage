from contentProcess import getDomain

def checkDomainMismatch(headerData):
    fromDomain = getDomain(headerData['From'])
    returnDomain = getDomain(headerData['ReturnPath'])
    if fromDomain is None or returnDomain is None:
        return False
    elif (fromDomain != returnDomain):
        return True
    else:
        return False

