#!/usr/bin/env python3
"""mapper.py"""
import sys

datafile=sys.argv[1]
country_name=sys.argv[2]

with open(country_name, 'r') as file:
    for line in file:
        line = line.strip()
        print(f"{line}")

with open(datafile, 'r') as file:
    for line in file:
        line = line.strip()
        line=eval(line)
        print(f"{line[1]}\t{line[2:]}")