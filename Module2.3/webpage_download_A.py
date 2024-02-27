import os
from urllib.request import Request, urlopen
import re

# URL of the wikipedia page
url = "https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic"

# Requesting the webpage
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# Reading the webpage
webpage = urlopen(req).read()

# Decoding the webpage
webpage = webpage.decode('utf-8')

# Pattern for matching the url. Instead of India there can be other countries as well.. Also the year can be different. Month name may or may not be present but year will definately be present. 
# <a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_India_(January%E2%80%93May_2020)"
# <a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_England_(2021)"
countries = ["India", "Australia", "Malaysia", "England", "Singapore"]

# Create patterns for each country
pattern = re.compile(r'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_'+countries[0]+'_\((.*?)\)"')
pattern = re.compile(r'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_'+countries[1]+'_\((.*?)\)"')
pattern = re.compile(r'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_'+countries[2]+'_\((.*?)\)"')
pattern = re.compile(r'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_'+countries[3]+'_\((.*?)\)"')
pattern = re.compile(r'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_'+countries[4]+'_\((.*?)\)"')

# Data URLs
dataUrls = {}
countryAndFileMap = {}

for country in countries:
    pattern = re.compile(r'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_'+country+'_\((.*?)\)"')
    # Get the matched pattern
    matches = pattern.findall(webpage)

    countryAndFileMap[country] = []

    # Construct the data URL for each match
    for match in matches:
        urlForCountry = "https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_"+country+"_(" + match + ")"
        # extract January May_2022 from January%E2%80%93May_2020 
        match = match.replace("%E2%80%93", "_")

        # key is country(match)
        key = country + '(' + match + ')'

        # Check if the URL is already present in the list. Also check if the key is already present in the dictionary
        dataUrls[key] = urlForCountry

        # Append the key to the list
        countryAndFileMap[country].append(key)

# # Print the data URLs
# for country in countries:
#     print("Data URLs for " + country + " are: ")
#     for url in dataUrls[country]:
#         print(url)

# Write the data URLs to a file so that it is read by the next program as key-value pairs
with open("dataUrls.txt", "w") as file:
    # key:URL1,URL2,URL3 for dataUrls
    for key in dataUrls:
        file.write(key + "|" + dataUrls[key] + "\n")

# Fetch the data from the URLs and save it in a file in folder named "webpages"
# Create a folder named "webpages" if it does not exist
if not os.path.exists("webpages"):
    os.makedirs("webpages")

for key in dataUrls:
    # Requesting the webpage
    req = Request(dataUrls[key], headers={'User-Agent': 'Mozilla/5.0'})

    # Reading the webpage
    webpage = urlopen(req).read()

    # Decoding the webpage
    webpage = webpage.decode('utf-8')

    # Write the webpage to a file
    with open("webpages/"+key+".html", "w") as file:
        file.write(webpage)
        file.close()

# call indiaParser1.py and indiaParser2.py for India values in countryAndFileMap
for country in countryAndFileMap:
    if country == "India":
        for filename in countryAndFileMap[country]:
            # replace '(' with '\(' and ')' with '\)'
            filename = filename.replace("(", "\(")
            filename = filename.replace(")", "\)")
            os.system("python3 indiaParser1.py " + filename)
            os.system("python3 indiaParser2.py " + filename)