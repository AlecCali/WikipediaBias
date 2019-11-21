import urllib3
from urllib.parse import urlparse
from tld import get_fld
from tld.utils import update_tld_names
from os import listdir

update_tld_names()

DEBUG = False

govdomains = []
with open('govdomains.txt', 'r') as f:
  govdomains = f.read().split()

news = ["nytimes.com", "washingtonpost.com", "wsj.com", "foxbusiness.com", "foxnews.com", "pbs.org", "npr.org", "cnn.com", "nbcnews.com", "msnbc.com", "abcnews.go.com", "cbsnews.com", "latimes.com", "newsweek.com", "time.com", "bloomberg.com", "reuters.com", "huffpost.com", "newyorker.com", "usatoday.com", "slate.com", "buzzfeed.com", "foreignpolicy.com"]
ngo = ["clintonfoundation.org", "amnesty.org", "hrw.org", "oxfam.org", "ned.org", "freedomhouse.org", "opensocietyfoundations.org", "cfr.org", "ndi.org", "mercycorps.org", "mei.org", "worldjusticeproject.org", "usip.org"]
cia = ["cia.gov"]


def fld(url):
  try:
    return get_fld(url)
  except:
    if DEBUG:
      print("Could not parse the following:", url)
    return ""

def get_domain(url):
  domain = fld(url)
  if domain == "archive.org":
    path = urlparse(url).path
    chunks = path.split('/')
    if chunks[0] != "web":
      return domain

    del chunks[:3]
    new_url = '/'.join(chunks)
    domain = fld(new_url)
  return domain

def cite(country, sources): 
  result = {}
  urls = open(country, "r").read().split('\n')
  for url in urls:
    if url[-1] == '\n':
      print("Unexpected newline")
      return

    domain = get_domain(url)
    if domain != "":
      if domain in sources:
        if domain in result:
          result[domain] += 1
        else:
          result[domain] = 1
  return sum(result.values())

PATH = "refs/"
for country in listdir(PATH):
  if "swp" in country:
    continue
  print("Citations for", country)
  print("news:", cite(PATH + country, news))
  print("cia: ", cite(PATH + country, cia))
  print("ngo: ", cite(PATH + country, ngo))
  print("gov: ", cite(PATH + country, govdomains))

# for country in listdir(PATH):
#   if "swp" in country:
#     continue
#   print(country, len(open(PATH + country).readlines()))

# URLs =open("refs/Afghanistan", "r")
# for line in URLs.readlines():
#   source = urlparse(line)
#   if source.netloc in ngolst:
#     if source.netloc in result:
#       result[source.netloc] = result[source.netloc] + 1
#     else:
#      result.update({source.netloc : 1})
#      print(result)

#URLs =open("refs/Bolivia", "r")
#for line in URLs.readlines():
#  source = urlparse(line)
#  if source.netloc in cia:
#    if source.netloc in result:
#      result[source.netloc] = result[source.netloc] + 1
#    else:
#       result.update({source.netloc : 1})
#print(result)

# URLs =open("refs/Afghanistan", "r")
# for line in URLs.readlines():
#   source = urlparse(line)
#   if source.netloc in govdomains:
#     if source.netloc in result:
#       result[source.netloc] = result[source.netloc] + 1
#     else:
#       result.update({source.netloc : 1})
# print(result)

