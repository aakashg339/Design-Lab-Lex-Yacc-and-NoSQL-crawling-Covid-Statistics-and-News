# #!/usr/bin/env python
# Reducer
import sys

def change(a,b):
    if a==0 or b==0:
        return "N/A"
    return f"{((b-a)/a)*100:.2f}%"

dict1= {"active cases":0,"new cases":0,"new deaths":0,"new recoveries":0}
dict2= {"active cases":0,"new cases":0,"new deaths":0,"new recoveries":0}



def form_date(line):
    month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    st_date=line.strip()
    dd,mm,yy=st_date.split('-')
    if mm[0]=='0':
        mm=mm[1]
    mm=int(mm)
    st_date=f'{month[mm-1]} {dd}, {yy}'
    return st_date


def closeness_func(per,all):
    per_float = float(per.rstrip('%'))
        
    if per== "N/A":
        return "N/A"
    closest_country = None
    closest_percentage = None
    min_diff = float('inf')
    for country, percentage in all:
        percentage_float = float(percentage.rstrip('%'))
        diff = abs(percentage_float - per_float)
        if diff < min_diff:
            min_diff = diff
            closest_country = country
            closest_percentage = percentage

    # print(f"Closest: {closest_country} ({closest_percentage})")
    return f"{closest_country} ({closest_percentage})"
            

# filenamwe=sys.argv[1]
with open('user.txt') as f:
    data=f.readlines()
    user_country=data[0].strip()
    st_date=form_date(data[1])
    end_date=form_date(data[2])
    # print(st_date)

comparision={}



for line in sys.stdin:
    info=line.strip().split('\t')
    # print(info[0])
    if info[0]==user_country:
        if info[1]==st_date:
            dict1["active cases"]=int(info[2][info[2].rindex(',')+3:-1])
            dict1["new cases"]=int(info[3][info[3].rindex(',')+3:-1])
            dict1["new deaths"]=int(info[4][info[4].rindex(',')+3:-1])
            dict1["new recoveries"]=int(info[5][info[5].rindex(',')+3:-1])
        elif info[1]==end_date:
            dict2["active cases"]=int(info[2][info[2].rindex(',')+3:-1])
            dict2["new cases"]=int(info[3][info[3].rindex(',')+3:-1])
            dict2["new deaths"]=int(info[4][info[4].rindex(',')+3:-1])
            dict2["new recoveries"]=int(info[5][info[5].rindex(',')+3:-1])
    else:
        if info[1]==st_date:
            d1=int(info[2][info[2].rindex(',')+3:-1])
            d2=int(info[3][info[3].rindex(',')+3:-1])
            d3=int(info[4][info[4].rindex(',')+3:-1])
            d4=int(info[5][info[5].rindex(',')+3:-1])
        elif info[1]==end_date:
            e1=int(info[2][info[2].rindex(',')+3:-1])
            e2=int(info[3][info[3].rindex(',')+3:-1])
            e3=int(info[4][info[4].rindex(',')+3:-1])
            e4=int(info[5][info[5].rindex(',')+3:-1])
            comparision[info[0]]={"active cases":change(d1,e1),"new cases":change(d2,e2),"new deaths":change(d3,e3),"new recoveries":change(d4,e4)}

# print(dict1)
# print(dict2)
# print(comparision)
closest_active_cases=[]
closer_new_cases=[]
closer_new_deaths=[]
closer_new_recoveries=[]
for country, values in comparision.items():
    closest_active_cases.append((country, values['active cases']))
    closer_new_cases.append((country, values['new cases']))
    closer_new_deaths.append((country, values['new deaths']))
    closer_new_recoveries.append((country, values['new recoveries']))

all=[closest_active_cases,closer_new_cases,closer_new_deaths,closer_new_recoveries]

print(f"Country: {user_country}")
headings=["active cases","new cases","new deaths","new recoveries"]
print(f"{'':<14}\t{st_date:>13}\t{end_date:>15}\t\tPercentage chnage\tClosest match")
for i in range(4):
    a=dict1[headings[i]]
    b=dict2[headings[i]]
    per_change=change(a,b)
    close_ans=closeness_func(per_change,all[i])
    print(f"{headings[i]:<14}\t{dict1[headings[i]]:>13}\t{dict2[headings[i]]:>15}\t\t{per_change:>14}\t{close_ans:>20}")


# sorted_data = sorted(comparision.items(), key=lambda x: x[1]['active cases'])

# for country, values in sorted_data:
#     print(country, values)