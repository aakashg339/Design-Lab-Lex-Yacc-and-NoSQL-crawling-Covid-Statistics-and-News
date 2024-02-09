import os
print("WELCOME TO MODULE 3.1 SHOWING DETAILS OF COVID DATA")

print("1. Show the details of statistics of a country and the world's percentage")
print("2. Show the details of statistics of a country over a specified period of time")

print("Enter your choice: ", end="")
choice = int(input())

if choice == 1:
    print("Enter the country name: ", end="")
    country = input().strip().lower()
    country = country[0].upper() + country[1:]

    print("press X to see all fields, else press enter to continue:")
    inp=input().strip().lower()
    if inp=='x':
        fields_list=['total cases', 'active cases', 'total deaths', 'total recovered', 'total tests','deaths/ 1m pop', 'tests/ 1m pop', 'new cases', 'new deaths', 'new recovered']
        print("Fields: ",fields_list)
    

    print("Enter the number of fields you want to see: ", end="")
    n = int(input())
    fields_list = []
    for i in range(n):
        print("enter field name:  ", end="")
        fields = input().strip().lower()
        fields_list.append(fields)
   
    with open('./A/country.txt', 'w') as f:
        f.write(country)
    

    with open('./A/fields.txt', 'w') as f:
        for field in fields_list:
            f.write(field + '\n')

    # os.system('')
    # run the make command of folder a
    os.system('make -C ./A')
    print("The details are shown in the file ./A/output.txt")

elif choice == 2:
    