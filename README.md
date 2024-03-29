# Design-Lab-Lex-Yacc-and-NoSQL Project 

## Project : Lex Yacc and NoSQL - crawling Covid Statistics and News

## Repository Link : https://github.com/aakashg339/Design-Lab-Lex-Yacc-and-NoSQL-crawling-Covid-Statistics-and-News

## Distribution of work : 

- Aakash Gupta(23CS60R22) : Module 2 (2nd part) and Module 3.2
- Rajdeep Ghosh(23CS60R10) : Module 1 and Module 3.1 and Module 4
- Satya Prakash Nayak(23CS60R05) : Module 2 (1st part) and Module 3.2


## How to run the code:


The entire project has a single entry point which is the file 'driver.py' to run the whole project.

```bash
cd Design-Lab-Lex-Yacc-and-NoSQL-crawling-Covid-Statistics-and-News
python3 driver.py
```

## Project Description:

The project is divided into 4 modules. 
- Module 1 : Crawling Covid-19 statistics from the website https://www.worldometers.info/coronavirus/ (for all countries and individual countries over a period of time)

- Module 2 : Crawling Covid-19 news wiki page https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic containing date wise text data of the Covid-19 news and also for multiple countries.
  - Module 2.1 and 2.2 : Extracting the worldwide news and responses for all times.
  - Module 2.3  : Extracting the news and responses for a particular country over a period of time.

- Module 3 : 
    - Module 3.1 : Using NOSQL database to give the results of the statistics and news in a structured format for the queries related to MODULE 1 
    - Module 3.2 : Using NOSQL database to give the results of the statistics and news in a structured format for the queries related to MODULE 2

- Module 4: Combining the entire project and creating a user interface for the user to interact with the database and get the required information.

# Work Done:

## Module 1 

- All Countries table -> Extract the data from the mentioned fields for all the countries and store it in a NoSQL database (output.txt). There is a driver.py to run the code. The grammars are mentioned in the file 'extract.py' and the output is stored in 'output.txt'. LEXX and YACC are used to parse the data.

- Individual Country  -> Extract the data for the 4 fields mentioned for a particular country mentioned in worldmeters_countrylist.txt . The 'driver.py' is used to run the code. The grammars are mentioned in the file 'extract_activecases.py' , 'extract_newcases.py' , 'extract_newdeaths.py' and 'extract_newrecoveries.py' . After that the outputs are merged into a single file present in "merged_files" as 'mfile_countryname.txt'. LEXX and YACC are used to parse the data.

*NOTE* All countries mentioned in worldmeters_countrylist.txt are do not have all of the 4 fields. Hence I modified the list to include only those countries which have all the 4 fields. 


## Module 2

### Module 2.1 and 2.2
This part of the module crawls the Wikipedia link: https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic and then extracts worldwide news and responses for all times.

- To obtain all the required Wikipedia webpages, we first download the main wiki page using Mainpage_download.py.
- From the main wiki page, we extract all the timelines and response pages present on that page using links_extract.py.
- Finally, using extract_info.py, we extract all the response pages one by one, categorized by their respective month names, which are then organized inside their respective years. For this process, the extracted parts contain H2 headers like "Reactions and measures in Europe", H3 headers like "1 April", and all the list and paragraph contents under them.
- For this part, we have utilized modules such as ply.lex, ply.yacc, os, and re.

### Module 2.3
Completed part 2.3 for India. Currently it works only for India and for few Australia page.
- HTML file of each country is of different format.
- Within each file also the structure can change.
- Therefore used two files 'IndiaParser1.py' and 'IndiaParser2.py' to parse the data and a seperate one for Australia.

First extracted the required webpages and then extracting the data. 

## Module 3.1 

There are broadly two parts to this module.

- Part 1 : display the statistics of a particular country for a set of fields mentioned. The user is asked about the country name and set of fields . These are stored in files and feed into the mapper along with the raw data we obtained from module 1. The mapper passes the data to the reducer which inturn preprocess and filters and send it to the reducer for the final output. The output is stored in a file named 'output_1.txt' . 

- Part 2 : display the details of 4 fields of a particular country. The user is asked about the name of the country as well as start and end date. The country, start date and end date are written in a file which is to be feed into the mapper. Also all country names are written in a file which is to be feed into the mapper along with date. The mapper passes the data to the reducer which inturn preprocess and filters and send it to the reducer for the final output.The logic of closest country in respect to percentage change is also done int the reducer. The output is stored in a file named 'output_2.txt' . 

Outputs can also be displayed from the menu. 


## Module 3.2

There are 2 Parts present in this module. 
- Part 1 : Displays all the worldwide responses given a time range. The user is asked about (start month start year end month end year). All the responces were extracted and saved in module 2. Given the time range, goes through all the subfolders and extracts all txt files which are inbetween those time range and puts all text in a single txt file. This is then fed to mapper. The mapper passes the data to the reducer which preprocess the data and sends it to the reducer for the final output. The output is displayed on terminal.

- Part 2: Displays the news and responses for a particular country over a period of time. The user is asked about the name of the country as well as start and end date. The country, start date and end date are written in a file which is to be feed into the mapper. The inputs are feed into the mapper along with date. The mapper passes the data to the reducer which inturn preprocess and filters and send it to the reducer for the final output. The logic of closest country in respect to percentage change is also done int the reducer. The output is stored in a file named 'output_2.txt' .


## Module 4

A menu is created to interact with the user. The user can select the module and the required query. The entire project can be accessed from the menu. The user can also see the output of the queries from the menu.
GUI part has been done only for Module 3.1 for displaying the outputs. But is not fully functional.Hence scope for improvement is there.
GUI is done using tkinter library in python.


## SCREENSHOTS of the project:

![image](assets/1.png)
![image](assets/2.png)
![image](assets/3.png)
![image](assets/4.png)
![image](assets/5.png)
![image](assets/6.png)

## Team Members:

<table>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/aakashg339/"><img src="https://avatars.githubusercontent.com/u/141503528?v=4" width="100px;" alt=""/><br /><sub><b>Aakash Gupta</b></sub></a><br /><a href="https://github.com/aakashg339/Design-Lab-Lex-Yacc-and-NoSQL-crawling-Covid-Statistics-and-News/commits/master/?author=aakashg339" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/rajdeep-ghosh2000rg/"><img src="https://avatars.githubusercontent.com/u/58541505?v=4" width="100px;" alt=""/><br /><sub><b>Rajdeep Ghosh</b></sub></a><br /><a href="https://github.com/aakashg339/Design-Lab-Lex-Yacc-and-NoSQL-crawling-Covid-Statistics-and-News/commits/master/?author=Rajdeep-G" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/MELL0WED"><img src="https://avatars.githubusercontent.com/u/105032869?v=4" width="100px;" alt=""/><br /><sub><b>Satya Prakash Nayak</b></sub></a><br /><a href="https://github.com/aakashg339/Design-Lab-Lex-Yacc-and-NoSQL-crawling-Covid-Statistics-and-News/commits/master/?author=MELL0WED" title="Documentation">📖</a></td>
  </tr>
</table>
