# #!/usr/bin/env python
# Reducer
import sys

def change(a,b):
    if a==0 or b==0:
        return "N/A"
    return f"{((b-a)/a)*100:.2f}%"

dict1= {"active cases":0,"new cases":0,"new deaths":0,"new recoveries":0}
dict2= {"active cases":0,"new cases":0,"new deaths":0,"new recoveries":0}
i = 0
dict = {}
st_date = ""
end_date = ""
cc=0
for line in sys.stdin:
    line=line.strip().split('\t')
    # print(line)
    date=line[0]
    data=line[2]
    type=line[1]
    if cc<4:
        dict1[type]+=int(data)
        st_date=date 
    else:
        dict2[type]+=int(data) 
        end_date=date
    cc+=1

headings=["active cases","new cases","new deaths","new recoveries"]
print(f"{'':<14}\t{st_date:>13}\t{end_date:>15}\t\tPercentage chnage")
for i in range(4):
    a=dict1[headings[i]]
    b=dict2[headings[i]]
    per_change=change(a,b)
    print(f"{headings[i]:<14}\t{dict1[headings[i]]:>13}\t{dict2[headings[i]]:>15}\t\t{per_change}")
