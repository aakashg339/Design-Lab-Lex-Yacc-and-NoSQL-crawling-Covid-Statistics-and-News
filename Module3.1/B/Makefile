all:
	chmod +x ./mapper.py ./reducer.py ./combiner.py
	
	
	(python3 ./mapper.py ../../Module1/individual_country/output_activecases.txt details.txt | python3 ./combiner.py & python3 ./mapper.py ../../Module1/individual_country/output_newcases.txt details.txt | python3 ./combiner.py & python3 ./mapper.py ../../Module1/individual_country/output_newdeaths.txt details.txt | python3 ./combiner.py & python3 ./mapper.py ../../Module1/individual_country/output_newrecoveries.txt details.txt | python3 ./combiner.py) | sort | python3 reducer.py > output_1.txt
	