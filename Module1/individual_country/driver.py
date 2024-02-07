

import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

# user_country=(input("Enter the country: "))
# user_country=user_country.strip().lower()
user_country = "italy"

url=f'https://www.worldometers.info/coronavirus/country/{user_country}/'
req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f=open('webpage.html','w',encoding="utf-8")
f.write(mydata)
f.close
