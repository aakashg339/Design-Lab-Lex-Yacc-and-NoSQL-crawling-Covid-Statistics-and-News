import os
print("WELCOME TO LEX-YACC BASED COVID-19 DATA ANALYSIS PROJECT ")
print("HERE's WHAT WE HAVE FOR YOU: ")
print("Module 1: Extracting data from WORLDOMETER website [a. Tabular data for all countries, b. Individual country data from scripts]")
print("Module 2: Extracting data from WIKIPEDIA website")
print("Module 3: USING MAPPER_COMBINER-REDUCER to show the result of queries")

print("\nLESSS GO !!!!!!!!!!!!!!!!!\n")

while True:
    print ("PRESS 1 for WORLDOMETER DATA EXTRACTION & QUERIES")
    print ("PRESS 2 for WIKIPEDIA DATA EXTRACTION & QUERIES")
    print ("PRESS e/E to exit")

    choice= input()

    if choice=="e" or choice=="E":
        break

    if choice=="1":
        print("RAJ")
        x=os.getcwd()
        print(x)
        if "Module3.2/A" in x:
            os.chdir("..")                        
        if "Module3.2" in x:
            os.chdir("..")
        if "Module3.1" not in x:
            os.chdir("Module3.1")
        os.system('python3 menu.py')
        
    if choice=="2":
        print("1. PRESS 1 for WORLDWIDE NEWS (global) data")
        print("2. PRESS 2 for COUNTRYWISE NEWS data for specific country")
        print("PRESS b/B to go back to main menu")
        print("PRESS e/E to exit ")
        country_choice= input()
        if country_choice=="1":
            print("SATYA")
            x=os.getcwd()
            if "Module3.1" in x:
                os.chdir("..")
            if "Module3.2/A" not in x:
                if "Module3.2" in x:
                    os.chdir("A")
                else:
                    os.chdir("Module3.2/A")
            os.system('python3 menu.py')
        if country_choice=="2":
            print("AAKASH")
            x=os.getcwd()
            if "Module3.1" in x:
                os.chdir("..")
            if "/A" in x:
                print("A")
                os.chdir("..")
            if "Module3.2" not in x:
                os.chdir("Module3.2")
            os.system('python3 menu.py')
        if country_choice=="b" or country_choice=="B":
            continue
        if country_choice=="e" or country_choice=="E":
            exit()