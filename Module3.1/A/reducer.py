# #!/usr/bin/env python
# Reducer
import sys


def per(a, b):
    if a==None or b==None:
        return None
    a=a.replace(',','')
    b=b.replace(',','')
    a = float(a)
    b = float(b)
    return round((a / b) * 100, 2)

current_key = None
current_count = 0
i = 0
dict = {}
for line in sys.stdin:
    if i == 0:
        country_output = line
        country_output = country_output.strip()
        i += 1
        continue
    if i == 1:
        i += 1
        continue
    if i == 2:
        _, lebels = line.strip().split('\t')
        lebels = eval(lebels)
        i += 1
        continue
    country, data = line.strip().split('\t')
    data = eval(data)
    dict[country] = {lebels[0]: data[0], lebels[6]: data[6], lebels[2]: data[2], lebels[4]: data[4], lebels[10]: data[10], lebels[9]: data[9], lebels[11]: data[11], lebels[1]: data[1], lebels[3]: data[3], lebels[5]: data[5]}
    

print(f'DETAILS OF {country_output} AND WORLD\'s PERCENTAGE')
# print(dict[country_output])
# print(dict['World'])
for x in dict[country_output]:
    cc=dict[country_output][x]
    cw=dict['World'][x]
    res=per(cc,cw)
    ss="None"
    if res!=None:
        print(f'{x:<30}\t{cc:<20}{res}%')
    else:
        if cc==None:
            cc="None"
        print(f'{x:<30}\t{cc:<20}{ss}')
