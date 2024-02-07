# combiner.py
import sys


month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
reqd_dates=[]
i=0
for line in sys.stdin:
    if i==0:
        st_date=line.strip()
        dd,mm,yy=st_date.split('-')
        if mm[0]=='0':
            mm=mm[1]
        mm=int(mm)
        st_date=f'{month[mm-1]} {dd}, {yy}'
        i+=1
        continue
    if i==1:
        end_date=line.strip()
        dd,mm,yy=end_date.split('-')
        if mm[0]=='0':
            mm=mm[1]
        mm=int(mm)
        end_date=f'{month[mm-1]} {dd}, {yy}'
        i+=1
        continue
    line = line.strip()
    line=eval(line)
    date=line[0]
    data=line[2]


    if st_date==date:
        print(f"{date}\t{line[1]}\t{data}")
    if end_date==date:
        print(f"{date}\t{line[1]}\t{data}")




