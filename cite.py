import os
import wikipedia

COUNTRIES = "countries"
BIN = "refsnew/"

def country_list():
  with open(COUNTRIES) as f:
    countries = f.read().strip().split('\n')
  return countries

def verify_countries():
  i = 196
  countries = country_list()
  while i < len(countries):
    name = countries[i]
    print(name, wikipedia.page(name))
    i += 1

def cite_countries():
  if not os.path.exists(BIN):
    os.mkdir(BIN)

  countries = country_list()
  for name in countries:
    print(wikipedia.page(name))

    filename =  BIN + name
    with open(filename, 'w') as f:
      f.truncate(0)
      page = wikipedia.page(name)
      f.write('\n'.join(page.references))

if __name__ == '__main__':
  cite_countries()
