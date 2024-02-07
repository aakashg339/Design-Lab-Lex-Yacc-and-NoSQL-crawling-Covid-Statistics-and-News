all:
	chmod +x ./mapper.py ./reducer.py ./combiner.py
	
	
	python3 ./mapper.py ../../Module1/allcountries_table/output.txt country.txt | python3 combiner.py | python3 reducer.py > output_1.txt
	