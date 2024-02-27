# Design-Lab-Lex-Yacc-and-NoSQL Project 

## Project : Lex Yacc and NoSQL - crawling Covid Statistics and News


## Distribution of work : 

- Aakash Gupta : Module 2 (2nd part) and Module 3.2
- Rajdeep Ghosh : Module 1 and Module 3.1
- Satya Prakash Nayak : Module 2 (1st part) and Module 4


## How to run the code:
(since its incomplete, the code needs to be run separately for each module)


For module 1 and its queries : 

```
cd Module3.1
python3 menu.py
```

Please enter valid inputs as mentioned in the menu.
## Project Description:

The project is divided into 4 modules. 
- Module 1 : Crawling Covid-19 statistics from the website https://www.worldometers.info/coronavirus/ (for all countries and individual countries over a period of time)

- Module 2 : Crawling Covid-19 news wiki page https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic containing date wise text data of the Covid-19 news and also for multiple countries.

- Module 3 : 
    - Module 3.1 : Using NOSQL database to give the results of the statistics and news in a structured format for the queries related to MODULE 1 
    - Module 3.2 : Using NOSQL database to give the results of the statistics and news in a structured format for the queries related to MODULE 2

- Module 4: Combining the entire project and creating a user interface for the user to interact with the database and get the required information.

## Module 1 

- All Countries table -> Extract the data from the mentioned fields for all the countries and store it in a NoSQL database (output.txt). There is a driver.py to run the code. The grammars are mentioned in the file 'extract.py' and the output is stored in 'output.txt'

- Individual Country  -> Extract the data for the 4 fields mentioned for a particular country mentioned in worldmeters_countrylist.txt . The 'driver.py' is used to run the code. The grammars are mentioned in the file 'extract_activecases.py' , 'extract_newcases.py' , 'extract_newdeaths.py' and 'extract_newrecoveries.py' . After that the outputs are merged into a single file present in "merged_files" as 'mfile_countryname.txt'.

*NOTE* All countries mentioned in worldmeters_countrylist.txt are do not have all of the 4 fields. Hence I modified the list to include only those countries which have all the 4 fields. 


## Module 2


## Module 3.1 

There are broadly two parts to this module.
- Part 1 : display the statistics of a particular country for a set of fields mentioned. The user is asked about the country name and set of fields . These are stored in files and feed into the mapper along with the raw data we obtained from module 1. The mapper passes the data to the reducer which inturn preprocess and filters and send it to the reducer for the final output. The output is stored in a file named 'output_1.txt' . 

- Part 2 : display the details of 4 fields of a particular country. The user is asked about the name of the country as well as start and end date. The country, start date and end date are written in a file which is to be feed into the mapper. Also all country names are written in a file which is to be feed into the mapper along with date. The mapper passes the data to the reducer which inturn preprocess and filters and send it to the reducer for the final output.The logic of closest country in respect to percentage change is also done int the reducer. The output is stored in a file named 'output_2.txt' . 

Outputs can also be displayed from the menu. 

A menu is also provided to display the outputs related to module 1 from worldmeters_countrylist.txt .


## Module 3.2


## Team Members:

<table>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/aakashg339/"><img src="https://avatars.githubusercontent.com/u/141503528?v=4" width="100px;" alt=""/><br /><sub><b>Aakash Gupta</b></sub></a><br /><a href="https://github.com/aakashg339/Design-Lab-Lex-Yacc-and-NoSQL-crawling-Covid-Statistics-and-News/commits/master/?author=aakashg339" title="Documentation">📖</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/rajdeep-ghosh2000rg/"><img src="https://avatars.githubusercontent.com/u/58541505?v=4" width="100px;" alt=""/><br /><sub><b>Rajdeep Ghosh</b></sub></a><br /><a href="https://github.com/aakashg339/Design-Lab-Lex-Yacc-and-NoSQL-crawling-Covid-Statistics-and-News/commits/master/?author=Rajdeep-G" title="Documentation">📖</a></td>
    <td align="center"><a href=""><img src="https://avatars.githubusercontent.com/u/105032869?v=4" width="100px;" alt=""/><br /><sub><b>Satya Prakash Nayak</b></sub></a><br /><a href="" title="Documentation">📖</a></td>
  </tr>
</table>
