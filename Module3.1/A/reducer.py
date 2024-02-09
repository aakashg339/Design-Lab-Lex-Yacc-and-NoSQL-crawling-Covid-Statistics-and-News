# #!/usr/bin/env python
# Reducer
import sys


def per(a, b):
    if a == None or b == None:
        return None
    a = a.replace(',', '')
    b = b.replace(',', '')
    a = float(a)
    b = float(b)
    return round((a / b) * 100, 2)


current_key = None
current_count = 0
i = 0
reqd_fields = []
dict = {}
for line in sys.stdin:
    if i == 0:
        country_output = line
        country_output = country_output.strip()
        print(f'Country: {country_output}')
        i += 1
        continue
    if i == 1:
        line = (line.strip().split('\t'))
        reqd_fields = eval(line[0])
        i += 1
        continue
    if i == 2:
        _, lebels = line.strip().split('\t')
        lebels = eval(lebels)
        i += 1
        continue
    country, data = line.strip().split('\t')
    # print(f'{country}\t{data}')
    data = eval(data)
    dict[country] = {lebels[0].lower(): data[0], lebels[6].lower(): data[6], lebels[2].lower(): data[2], lebels[4].lower(): data[4], lebels[10].lower()
        : data[10], lebels[9].lower(): data[9], lebels[11].lower(): data[11], lebels[1].lower(): data[1], lebels[3].lower(): data[3], lebels[5].lower(): data[5]}

# print(dict)
for i in range(len(reqd_fields)):
    reqd_fields[i] = reqd_fields[i].strip().lower()

# print(dict)

xx=''
print(f'DETAILS OF {xx:<20}{country_output:<20} AND WORLD\'s PERCENTAGE\n')

reqd_country_det=dict[country_output]
world_det=dict['World']

for x in reqd_fields:
    cc=reqd_country_det[x]
    cw=world_det[x]
    res=per(cc,cw)
    ss="None"
    if res!=None:
        print(f'{x:<30}\t{cc:<20}{res}%')
    else:
        if cc==None:
            cc="None"
        print(f'{x:<30}\t{cc:<20}{ss}')
