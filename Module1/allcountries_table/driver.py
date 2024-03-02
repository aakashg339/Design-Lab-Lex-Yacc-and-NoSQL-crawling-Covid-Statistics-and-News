

import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
from datetime import date



url="https://www.worldometers.info/coronavirus/"
req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f=open('webpage.html','w',encoding="utf-8")
f.write(mydata)
f.close

# os.system("python3 ./helper/stats.py")
today_date=date.today()
print("Extracting data from the webpage on ",today_date)
os.system("python3 extract.py")
print("EXTRACTION COMPLETED!")