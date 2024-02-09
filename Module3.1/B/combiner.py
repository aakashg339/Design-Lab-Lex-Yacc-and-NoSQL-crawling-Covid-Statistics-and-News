# combiner.py
import sys


month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
reqd_dates=[]
i=0
country=''
dict=[]
for line in sys.stdin:
    if i==0:
        i+=1
        country=line.strip()
        # print(f"{line.strip()}")
        continue
    if i==1: 
        st_date=line.strip()
        dd,mm,yy=st_date.split('-')
        if mm[0]=='0':
            mm=mm[1]
        mm=int(mm)
        st_date=f'{month[mm-1]} {dd}, {yy}'
        i+=1
        continue
    if i==2:
        end_date=line.strip()
        dd,mm,yy=end_date.split('-')
        if mm[0]=='0':
            mm=mm[1]
        mm=int(mm)
        end_date=f'{month[mm-1]} {dd}, {yy}'
        i+=1
        continue
    line = line.strip()
    elements = line.split('][')
  
    temp=[] 
    for element in elements:
        element=element.strip('[]')
        temp.append(element)
        if len(temp)==4:
            dt=temp[0][1:13]
            info=f'{temp[0]}\t{temp[1]}\t{temp[2]}\t{temp[3]}'
            dict.append((dt,info))
            # print(f"{dict}")


# print(dict)
send=[]
for a,b in dict:
    if a==st_date:
        print(f"{country}\t{a}\t{b}")
        # send.append(f"{country}\t{a}\t{b}")
        break   
for a,b in dict:
    if a==end_date:
        print(f"{country}\t{a}\t{b}")
        # send.append(f"{a}\t{b}")
        break
# print(send)


