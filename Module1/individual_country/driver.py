

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
print("Extracting data from the webpage on ",datetime.datetime.now())

for i in allcountries:
    i=i.lower()

    url=f'https://www.worldometers.info/coronavirus/country/{i}'
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('../Module1/individual_country/webpage.html','w',encoding="utf-8")
    # f=open(f'..Module1/individual_country/webpage.html','w',encoding="utf-8")
    f.write(mydata)
    f.close

# 

    os.system('python3 ../Module1/individual_country/extract_activecases.py')
    os.system('python3 ../Module1/individual_country/extract_newcases.py')
    os.system('python3 ../Module1/individual_country/extract_newdeaths.py')
    os.system('python3 ../Module1/individual_country/extract_newrecoveries.py')
    os.system(f'python3 ../Module1/individual_country/merge.py {i}')
    os.system('rm ../Module1/individual_country/webpage.html ../Module1/individual_country/output_activecases.txt ../Module1/individual_country/output_newcases.txt ../Module1/individual_country/output_newdeaths.txt ../Module1/individual_country/output_newrecoveries.txt')

print("EXTRACTION COMPLETED!")