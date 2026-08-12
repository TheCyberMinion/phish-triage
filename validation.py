import re
from contentProcess import getUrlDomain

def checkDomainMismatch(fromDomain, returnDomain):
    if fromDomain is None or returnDomain is None:
        return False
    elif (fromDomain != returnDomain):
        return True
    else:
        return False

def extractIOCS(text):
    if text is None:
        return {'urls' : [] , 'ips' : []}
    else:

        # make list of urls
        urls = re.findall(r'https?://[^\s<>"\']+', text)
        urls = list(dict.fromkeys(urls))

        # make list of ip's
        ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', text)
        ips = list(dict.fromkeys(ips))

        return {'urls' : urls , 'ips' : ips}

def checkURL(urlList, domain):
    if domain is None:
        return None
    else:
        totalDomains = len(urlList)
        validDomains = 0
        for rawURL in urlList:
            url = getUrlDomain(rawURL)
            if url == domain or url.endswith('.' + domain):
                validDomains += 1
        return totalDomains, validDomains