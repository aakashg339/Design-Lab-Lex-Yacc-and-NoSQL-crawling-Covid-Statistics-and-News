

import os,sys
import ply.lex as lex
import ply.yacc as yacc
from datetime import date
from urllib.request import Request, urlopen

# user_country=(input("Enter the name of country: "))
# user_country=sys.argv[1]
# user_country=user_country.strip().lower()
# user_country = "italy"
allcountries = ['canada', 'france','italy', 'mexico', 'russia', 'germany']
# allcountries = ['France', 'UK', 'Russia', 'Italy', 'Germany', 'Spain', 'Poland', 'Netherlands', 'Ukraine', 'Belgium',
#                         'USA', 'Mexico', 'Canada', 'Cuba', 'Costa Rica', 'Panama', 'India', 'Turkey', 'Iran', 'Indonesia',
#                         'Philippines', 'Japan', 'Israel', 'Malaysia', 'Thailand', 'Vietnam', 'Iraq', 'Bangladesh', 'Pakistan',
#                         'Brazil', 'Argentina', 'Colombia', 'Peru', 'Chile', 'Bolivia', 'Uruguay', 'Paraguay', 'Venezuela',
#                         'South Africa', 'Morocco', 'Tunisia', 'Ethiopia', 'Libya', 'Egypt', 'Kenya', 'Zambia', 'Algeria',
#                         'Botswana', 'Nigeria', 'Zimbabwe', 'Australia', 'Fiji', 'Papua New Guinea', 'New Caledonia', 'New Zealand'
#                         ]

import datetime
today_date=date.today()
print("Extracting data from the webpage on ",today_date)

for i in allcountries:
    i=i.lower()

    url=f'https://www.worldometers.info/coronavirus/country/{i}'
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('webpage.html','w',encoding="utf-8")
    f.write(mydata)
    f.close

# 

    os.system('python3 extract_activecases.py')
    os.system('python3 extract_newcases.py')
    os.system('python3 ./extract_newdeaths.py')
    os.system('python3 ./extract_newrecoveries.py')
    os.system(f'python3 ./merge.py {i}')
    os.system('rm webpage.html output_activecases.txt output_newcases.txt output_newdeaths.txt output_newrecoveries.txt')

print("EXTRACTION COMPLETED!")