from contentProcess import parseEmailHeader, getDmarcPolicy, processContent
from validation import checkDomainMismatch, extractIOCS, checkURL
from contentProcess import getDomain

def main():

    # assign the content of .eml file
    msg = processContent()

    # get dict of keys and data
    headerData = parseEmailHeader(msg)

    fromDomain = getDomain(headerData['From'])
    returnDomain = getDomain(headerData['ReturnPath'])

    # check1 -> from and return domain against each other should mismatch ideally
    domainCheck = checkDomainMismatch(fromDomain, returnDomain)

    # check2 -> get dmarcPolicy should be 'Pass'
    dmarcPolicy = getDmarcPolicy(headerData['AuthenticationResults'])

    # dict of url and Ip's
    iocs = extractIOCS(headerData['Body'])

    # check3 -> url located inside the email pass/fail
    totalURLS, passURLS  = checkURL(iocs['urls'], fromDomain)

if __name__ == '__main__':
    main()