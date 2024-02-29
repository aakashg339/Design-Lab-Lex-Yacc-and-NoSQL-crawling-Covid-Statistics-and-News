import os

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

countries = ["India", "Australia", "Malaysia", "England"]
# Menu
while True:
    print("Press 1 to see country list")
    print("Press 2 to see date range of a country")
    print("Press 3 to enter country and date, and see the information")
    print("Press 4 to exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for country in countries:
            print(country)
    elif choice == "2":
        country = input("Enter country: ")
        if country in countries:
            printDateRangeforCountry(country)
        else:
            print("Country not found")
    elif choice == "3":
        print("ToDo")
    elif choice == "4":
        break
    else:
        print("Invalid choice")