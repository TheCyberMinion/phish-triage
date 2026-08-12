import email, email.policy, email.utils
import re

def processContent(content):
    return email.message_from_bytes(content, policy=email.policy.default)

def parseEmailHeader(fileContent):
    content = processContent(fileContent)
    headerData = {}

    # keys and data
    headerData['From'] = content['From']
    headerData['Subject'] = content['Subject']
    headerData['ReturnPath'] = content['Return-Path']
    headerData['AuthenticationResults'] = content['Authentication-Results']

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

def getDmarcPolicy(authData):
    if authData is None:
        return None
    else:
        if matches := re.search(r'dmarc=[A-Za-z]+ \((?:p=([A-Za-z]+) sp=[A-Za-z]+ dis=[A-Za-z]+)\)', authData):
            return matches.group(1).upper()
        else:
            return None
    


    


