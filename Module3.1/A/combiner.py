# combiner.py
import sys



cur_nodes = None
cur_freq = 0
heads={}
i=0
list_fields=[]
cond=False
for line in sys.stdin:
    if i==0:
        print(f'{line.strip()}')
        i+=1
        continue
    if line.strip()=='#####':
        cond=True
        print(f'{list_fields}')
        continue
    else:
        line=line.strip()
        list_fields.append(line)
    if cond==True:
        country, data = line.strip().split('\t')
        data = eval(data)
        print(f'{country}\t{data}')



