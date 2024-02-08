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

for country in countries:
    dataUrls[country] = []

for country in countries:
    pattern = re.compile(r'<a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_'+country+'_\((.*?)\)"')
    # Get the matched pattern
    matches = pattern.findall(webpage)
    # Construct the data URL for each match
    for match in matches:
        urlForCountry = "https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_"+country+"_(" + match + ")"

        # Check if the URL is already present in the list
        if urlForCountry not in dataUrls[country]:
            dataUrls[country].append("https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_"+country+"_(" + match + ")")

# # Print the data URLs
# for country in countries:
#     print("Data URLs for " + country + " are: ")
#     for url in dataUrls[country]:
#         print(url)

# Write the data URLs to a file so that it is read by the next program as key-value pairs
with open("dataUrls.txt", "w") as file:
    # Country:URL1,URL2,URL3
    for country in countries:
        file.write(country + ":")
        # Not including the last comma
        for url in dataUrls[country][:-1]:
            file.write(url + ",")
        file.write(dataUrls[country][-1] + "\n")
    file.close()

# Fetch the data from the URLs and save it in a file in folder named "webpages"
# Create a folder named "webpages" if it does not exist
if not os.path.exists("webpages"):
    os.makedirs("webpages")

for country in countries:
    for url in dataUrls[country]:
        # Requesting the webpage
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        # Reading the webpage
        webpage = urlopen(req).read()

        # Decoding the webpage
        webpage = webpage.decode('utf-8')

        # Save the webpage in a file
        with open("webpages/"+country+"_"+url.split("/")[-1]+".html", "w") as file:
            file.write(webpage)
            file.close()