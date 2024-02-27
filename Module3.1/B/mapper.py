#!/usr/bin/env python3
"""mapper.py"""
import sys,os

datafile=sys.argv[1]
country_details=sys.argv[2]

with open(country_details, 'r') as file:
    i=0
    for line in file:
        line = line.strip()
        if i==0:
            i+=1
            print(f"{line}")
            # os.system(f'python3 ../../Module1/individual_country/driver.py {line}')
            continue
        print(f"{line}")

with open(datafile, 'r') as file:
    for line in file:
        line = line.strip()
        # line=eval(line)
        print(f"{line}")