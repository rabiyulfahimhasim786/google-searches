from googlesearch import search
import requests
from lxml.html import fromstring

#Link URL Title retriever usin request and formstring
def Link_title(URL):
  x = requests.get(URL)
  tree = fromstring(x.content)
  return tree.findtext('.//title')

company_name = input("Please provide the company name:")
query = int(input("Please give the appropriate value. 1 for Fundamental Analysis, 2 for News, 3 for Technical Analysis & 4 for Share Price Forecast:"))

if query == 1:
  print (company_name+" "+"Fundamental Analysis:")
  print (" ")
  for i in search(company_name,  tld='com', lang='en', num=1, start=0, stop=1, domains=['https://www.tickertape.in/'], pause=2.0):
    print ("\t"+i)

elif query == 2:
  print (company_name+" "+"News:")
  print (" ")
  for i in search(company_name+ 'News',  tld='com', lang='en', num=3, start=0, stop=3, pause=2.0, tpe='nws'):
    print ("\t"+"#"+" "+Link_title(i))
    print("\t"+i)
    print(" ")

elif query == 3:
  print (company_name+" "+"Technical Analysis:")
  print (" ")
  for i in search(company_name+ 'Technical Analysis',  tld='com', lang='en', num=3, start=0, stop=3, pause=2.0):
    print ("\t"+"#"+" "+Link_title(i))
    print("\t"+i)
    print(" ")
    
else:
  print (company_name+" "+"Share Price Forecast:")
  print (" ")
  for i in search(company_name+ 'share price forecast',  tld='com', lang='en', num=3, start=0, stop=3, pause=2.0):
    print ("\t"+"#"+" "+Link_title(i))
    print("\t"+i)
    print(" ")