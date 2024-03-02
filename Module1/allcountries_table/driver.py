

import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
from datetime import datetime, date



url="https://www.worldometers.info/coronavirus/"
req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f=open('../Module1/allcountries_table/webpage.html','w',encoding="utf-8")
f.write(mydata)
f.close

# os.system("python3 ./helper/stats.py")
import datetime
today_date=date.today()
print("Extracting data from the webpage on ",datetime.datetime.now())
os.system("python3 ../Module1/allcountries_table/extract.py")
print("EXTRACTION COMPLETED!")