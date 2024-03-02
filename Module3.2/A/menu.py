import os
import sys
def display_responses(start_month, start_year, end_month, end_year):
    os.system('python3 file1.py')
    os.system(f'python3 selected_files.py {start_month} {start_year} {end_month} {end_year}')
    os.system('cat store.txt | python3 mapper.py | python3 combiner.py | python3 reducer.py')
# Function to validate if the input is in the correct format and represents valid months
def validate_input(input_str):
    try:
        start_month, start_year, end_month, end_year = map(int, input_str.split())
        if not (1 <= start_month <= 12 and 1 <= end_month <= 12):
            return False
        return True
    except ValueError:
        return False

# Function to handle user input for the time range
def get_time_range():
    while True:
        try:
            # input_str = input("Enter starting month starting year ending month ending year (e.g., 4 2020 5 2022), or 'exit' to go back to the main menu: ")
            print("Enter starting month")
            start_month=int(input())
            print("Enter starting year")
            start_year=int(input())
            print("Enter ending month")
            end_month=int(input())
            print("Enter ending year")
            end_year=int(input())

            # if input_str.lower() == 'exit':
            #     return None
            # start_month, start_year, end_month, end_year = map(int, input_str.split())
            if not (1 <= start_month <= 12 and 1 <= end_month <= 12):
                print("Invalid month. Month should be between 1 and 12.")
                continue
            return start_month, start_year, end_month, end_year
        except ValueError:
            print("Invalid input format. Please enter all four values separated by spaces.")
            continue
        
# Main function to run the menu-driven program
def main():
    while True:
        print("WELCOME TO MODULE 3.2 SHOWING RESPONSES BETWEEN A TIME RANGE")
        print("\n1. Enter time range")
        print('\n2. Go Back')
        print("\n3. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            time_range = get_time_range()
            if time_range:
                start_month, start_year, end_month, end_year = time_range
                display_responses(start_month, start_year, end_month, end_year)
                print("Response stored in output.txt")

                print("Output is saved in output.txt. Do you want to see the output? (y/n)")
                cch= input()
                if cch == "y":
                    with open("output.txt", "r") as file:
                        print(file.read())

        elif choice == '2':
            None
        elif choice == '3':
            print("Exiting the program.")
            sys.exit()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
        print('\n\n')


if __name__ == "__main__":
    main()
