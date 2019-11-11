import urllib3
from urllib.parse import urlparse

govdomains = open("govdomains.txt", "r")
print(govdomains.read().split('\n'))
gd = govdomains.read().split('\n')
print(gd)

news = ["nytimes.com", "washingtonpost.com", "wsj.com", "foxbusiness.com", "foxnews.com", "pbs.org", "npr.org", "cnn.com", "nbcnews.com", "msnbc.com", "abcnews.go.com", "cbsnews.com", "latimes.com", "newsweek.com", "time.com", "bloomberg.com", "reuters.com", "huffpost.com", "newyorker.com", "usatoday.com", "slate.com", "buzzfeed.com", "foreignpolicy.com"]
ngolst = ["clintonfoundation.org", "amnesty.org", "hrw.org", "oxfam.org", "ned.org", "freedomhouse.org", "opensocietyfoundations.org", "cfr.org", "ndi.org", "mercycorps.org", "mei.org", "worldjusticeproject.org", "usip.org"]
cia = ["cia.gov"]
gov = ["usaid.gov", "voanews.com", "alhuraa.com", "rfa.org", "rferl.org", "radiotelevisionmarti.com", "radiofarda.com"]
allgov = gov + gd
result = dict()

URLs = open("refs/Afghanistan", "r")
for line in URLs.readlines():
    source = urlparse(line)
    if source.netloc in news:
        if source.netloc in result:
            result[source.netloc] += result[source.netloc]
        else:
            result.update({source.netloc : 1})
print(result)

URLs =open("refs/Afghanistan", "r")
for line in URLs.readlines():
    source = urlparse(line)
    if source.netloc in ngolst:
        if source.netloc in result:
            result[source.netloc] += result[source.netloc]
        else:
            result.update({source.netloc : 1})
print(result)

URLs =open("refs/Afghanistan", "r")
for line in URLs.readlines():
    source = urlparse(line)
    if source.netloc in cia:
        if source.netloc in result:
            result[source.netloc] += result[source.netloc]
        else:
            result.update({source.netloc : 1})
print(result)

URLs =open("refs/Afghanistan", "r")
for line in URLs.readlines():
    source = urlparse(line)
    if source.netloc in allgov:
        if source.netloc in result:
            result[source.netloc] += result[source.netloc]
        else:
            result.update({source.netloc : 1})
print(result)

