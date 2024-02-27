This part of the module crawls the Wikipedia link: https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic and then extracts worldwide news and responses for all times.

To obtain all the required Wikipedia webpages, we first download the main wiki page using Mainpage_download.py.

From the main wiki page, we extract all the timelines and response pages present on that page using links_extract.py.

Finally, using extract_info.py, we extract all the response pages one by one, categorized by their respective month names, which are then organized inside their respective years. For this process, the extracted parts contain H2 headers like "Reactions and measures in Europe", H3 headers like "1 April", and all the list and paragraph contents under them.

For this part, we have utilized modules such as ply.lex, ply.yacc, os, and re.
