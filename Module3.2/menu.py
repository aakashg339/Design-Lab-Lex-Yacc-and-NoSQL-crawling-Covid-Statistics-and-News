import os
import datetime

EXtRACTED_DATA_PATH = "../Module2.3/extractedData/"

def printDateRangeforCountry(country):
    # Get all the filenames in the extractedData folder
    extractedDataFiles = os.listdir(EXtRACTED_DATA_PATH)

    # Take files with India in the name
    indiaFiles = list(filter(lambda x: country in x, extractedDataFiles))


    # replace ( with \( and ) with \)
    indiaFiles = list(map(lambda x: x.replace("(", "\("), indiaFiles))
    indiaFiles = list(map(lambda x: x.replace(")", "\)"), indiaFiles))

    # print(indiaFiles)

    # With all the files with India in the name, run the shell command. For each file, the mapper and combiner will be run and the output will be sorted and then the reducer will be run
    # Create shell command
    shell_command = "("
    for file in indiaFiles:
        shell_command += f"cat {EXtRACTED_DATA_PATH}{file} | python3 3/mapper.py | sort | python3 3/combiner.py ;"
    shell_command += ") | sort | python3 3/reducer.py"

    # print(shell_command)


    # # Define the shell command as a string
    # shell_command = """
    # (cat ../Module2.3/extractedData/India\(2021\).txt | python3 3/mapper.py | sort | python3 3/combiner.py | python3 3/reducer.py)
    # """

    # Execute the shell command
    os.system(shell_command)

def printNewsInDateRange(country, startDate, endDate):
    # Get all the filenames in the extractedData folder
    extractedDataFiles = os.listdir(EXtRACTED_DATA_PATH)

    # Take files with India in the name
    indiaFiles = list(filter(lambda x: country in x, extractedDataFiles))


    # replace ( with \( and ) with \)
    indiaFiles = list(map(lambda x: x.replace("(", "\("), indiaFiles))
    indiaFiles = list(map(lambda x: x.replace(")", "\)"), indiaFiles))

    # With all the files with India in the name, run the shell command. For each file, the mapper and combiner will be run and the output will be sorted and then the reducer will be run
    # Create shell command
    shell_command = "("
    for file in indiaFiles:
        shell_command += f"cat {EXtRACTED_DATA_PATH}{file} | python3 4/mapper.py {startDate} {endDate} | sort | python3 4/combiner.py ;"
    shell_command += ") | sort | python3 4/reducer.py > output.txt"

    # Execute the shell command
    os.system(shell_command)

countries = ["India", "Australia", "Malaysia", "England"]
# Menu
while True:
    print("1. Run the queries on PRE-EXISTING data")
    print("2. EXTRACT data from web and then run the queries")
    # print("3. Go back to previous menu")
    print("Enter your choice: ", end="")

    extract_choice = (input())
    if extract_choice == 'e' or extract_choice == 'E':
        break
    if extract_choice != '1' and extract_choice != '2':
        print("Invalid choice. Please try again.")
        continue
    if extract_choice == '2':
        print("Extracting data from web...")
        # os.system('python3 ../Module1/allcountries_table/driver.py')
        # os.system('python3 ../Module2.3/webpage_download_A.py')


    print("Press 1 to see country list")
    print("Press 2 to see date range of a country")
    print("Press 3 to enter country and date, and see the information")
    print("Press 4 to exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        for country in countries:
            print(country)
    elif choice == "2":
        country = input("\nEnter country: ")
        country=country.lower()
        country=country[0].upper()+country[1:]
        if country in countries:
            printDateRangeforCountry(country)
        else:
            print("Country not found")
    elif choice == "3":
        country = input("\nEnter country: ")
        country=country.lower()
        country=country[0].upper()+country[1:]
        if country in countries:
            # Take date range from user
            print("Example date format: 01-April-2021")
            startDate = input("Enter start date (dd-Month-YYYY): ")
            endDate = input("Enter end date (dd-Month-YYYY): ")

            # Check if the date is in the correct format
            try:
                datetime.datetime.strptime(startDate, '%d-%B-%Y')
                datetime.datetime.strptime(endDate, '%d-%B-%Y')
            except:
                print("Invalid date")
                continue



            printNewsInDateRange(country, startDate, endDate)

            print("Output is saved in output.txt. Do you want to see the output? (y/n)")
            cch= input()
            if cch == "y":
                with open("output.txt", "r") as file:
                    print(file.read())


        else:
            print("Country not found")
    elif choice == "4":
        break
    else:
        print("Invalid choice")