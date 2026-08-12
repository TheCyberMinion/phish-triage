import email, email.policy, email.utils

def processContent(content):
    return email.message_from_bytes(content, policy=email.policy.default)

def parseEmailHeader(fileContent):
    content = processContent(fileContent)
    headerData = {}
    headerData['From'] = content['From']
    headerData['Subject'] = content['Subject']
    headerData['ReturnPath'] = content['Return-Path']
    return headerData

def getDomain(header):
    if header is None:
        return None
    else:
        _ , address =  email.utils.parseaddr(header)
        if '@' not in address:
            return None
        else:
            _ , domainName = address.rsplit('@', 1)
            return domainName.lower()



    


