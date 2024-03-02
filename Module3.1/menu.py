import os
print("Please press (g/G) for GUI and (c/C) for command line interface")
ch = input().strip().lower()
if ch == 'g':
    while True:
        print("1. Show the details of statistics of a country and the world's percentage")
        print("2. Show the details of statistics of a country over a specified period of time")
        print("Press b/B to go back to previous menu")

        print("Enter your choice: ", end="")
        choice = (input())

        if (choice) == '1':
            os.system('python3 ./gui_a.py')
        elif choice == '2':
            os.system('python3 ./gui_b.py')
        elif choice == 'b' or choice == 'B':
            break
        else:
            print("Invalid choice. Give again.")
            
        
elif ch == 'c':
    while True:
        print("\nWELCOME TO MODULE 3.1 SHOWING DETAILS OF COVID DATA")

        print("1. Show the details of statistics of a country and the world's percentage")
        print("2. Show the details of statistics of a country over a specified period of time")
        print("Press b/B to go back to previous menu")

        print("Enter your choice: ", end="")
        choice = (input())

        if choice == '1':
            print("\n1. Run the queries on PRE-EXISTING data")
            print("2. EXTRACT data from web and then run the queries")
            print("Enter your choice: ", end="")
            extract_choice = int(input())
            if extract_choice != 1 and extract_choice != 2:
                print("Invalid choice. Please try again.")
                continue
            if extract_choice == 2:
                os.system('python3 ../Module1/allcountries_table/driver.py')

            print("Enter the country name: ", end="")
            country = input().strip().lower()
            country = country[0].upper() + country[1:]

            print("press X to see all fields, else press enter to continue:")
            inp = input().strip().lower()
            if inp == 'x':
                fields_list = ['total cases', 'active cases', 'total deaths', 'total recovered',
                            'total tests', 'deaths/ 1m pop', 'tests/ 1m pop', 'new cases', 'new deaths', 'new recovered']
                print("Fields: ", fields_list)

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

            os.system('make -C ./A')
            print("The details are shown in the file ./A/output.txt")

            print("\nDo you want to see the output? (y/n): ", end="")
            ch = input().strip().lower()
            if ch == 'y':
                os.system('cat ./A/output_1.txt')
            else:
                print("The output is stored in the file ./A/output_1.txt")

        elif choice == '2':
            print("1. Run the queries on PRE-EXISTING data")
            print("2. EXTRACT data from web and then run the queries")
            print("Enter your choice: ", end="")
            extract_choice = int(input())
            if extract_choice != 1 and extract_choice != 2:
                print("Invalid choice. Please try again.")
                continue
            if extract_choice == 2:
                os.system('python3 ../Module1/individual_country/driver.py')
            allcountries = ['canada', 'france','italy', 'mexico', 'russia', 'germany']
            # allcountries = ['France', 'UK', 'Russia', 'Italy', 'Germany', 'Spain', 'Poland', 'Netherlands', 'Ukraine', 'Belgium',
                            # 'USA', 'Mexico', 'Canada', 'Cuba', 'Costa Rica', 'Panama', 'India', 'Turkey', 'Iran', 'Indonesia',
                            # 'Philippines', 'Japan', 'Israel', 'Malaysia', 'Thailand', 'Vietnam', 'Iraq', 'Bangladesh', 'Pakistan',
                            # 'Brazil', 'Argentina', 'Colombia', 'Peru', 'Chile', 'Bolivia', 'Uruguay', 'Paraguay', 'Venezuela',
                            # 'South Africa', 'Morocco', 'Tunisia', 'Ethiopia', 'Libya', 'Egypt', 'Kenya', 'Zambia', 'Algeria',
                            # 'Botswana', 'Nigeria', 'Zimbabwe', 'Australia', 'Fiji', 'Papua New Guinea', 'New Caledonia', 'New Zealand'
                            # ]
            print("All COUNTRIES DO NOT HAVE ALL THE MENTIONED 4 FIELDS. Hence this task haas been limited to the counttries that have all 4 fields. They are as follows: ")
            print(allcountries)


            print("\nEnter the country name: ", end="")
            country = input().strip().lower()

            print("Enter the start date in the format DD-MM-YYYY: ", end="")
            start_date = input().strip()
            print("Enter the end date in the format DD-MM-YYYY: ", end="")
            end_date = input().strip()

            with open('./B/user.txt', 'w') as f:
                f.write(country + '\n' + start_date + '\n' + end_date)

            for i in allcountries:
                i= i.lower()
                # if i != country:
                with open(f'./B/allcountries/{i}.txt', 'w') as f:
                    f.write(i + '\n' + start_date + '\n' + end_date)

            os.system('make -C ./B')

            print("\nDo you want to see the output? (y/n): ", end="")
            ch = input().strip().lower()
            if ch == 'y':
                os.system('cat B/output_B.txt')
            else:
                print("The output is stored in the file ./B/output_B.txt")

        elif choice == 'b' or choice == 'B':
            break
        else:
            print("Invalid choice. Please try again.")

        print("\nDo you want to continue? (y/n): ", end="")
        ch = input().strip().lower()
        if ch == 'n':
            break
        os.system('clear')

        print()

else:
    print("Invalid choice. Goodbye.")
    exit()