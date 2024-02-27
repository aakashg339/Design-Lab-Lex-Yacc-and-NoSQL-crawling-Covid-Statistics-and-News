all:
	chmod +x ./mapper.py ./reducer.py ./combiner.py
	



	(python3 ./mapper.py ../../Module1/individual_country/merged_files/mfile_canada.txt  ./allcountries/canada.txt  | python3 ./combiner.py & python3 ./mapper.py ../../Module1/individual_country/merged_files/mfile_france.txt  ./allcountries/france.txt | python3 ./combiner.py & python3 ./mapper.py ../../Module1/individual_country/merged_files/mfile_germany.txt  ./allcountries/germany.txt | python3 ./combiner.py & python3 ./mapper.py ../../Module1/individual_country/merged_files/mfile_italy.txt  ./allcountries/italy.txt  | python3 ./combiner.py & python3 ./mapper.py ../../Module1/individual_country/merged_files/mfile_mexico.txt  ./allcountries/mexico.txt  | python3 ./combiner.py & python3 ./mapper.py ../../Module1/individual_country/merged_files/mfile_russia.txt  ./allcountries/russia.txt  | python3 ./combiner.py) | python3 ./reducer.py  > output_B.txt



