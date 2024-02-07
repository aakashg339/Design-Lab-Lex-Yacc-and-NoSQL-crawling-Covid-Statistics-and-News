# combiner.py
import sys



cur_nodes = None
cur_freq = 0
heads={}
i=0
for line in sys.stdin:
    if i==0:
        print(f'{line}')
        i+=1
        continue
    country, data = line.strip().split('\t')
    data = eval(data)
    print(f'{country}\t{data}')



