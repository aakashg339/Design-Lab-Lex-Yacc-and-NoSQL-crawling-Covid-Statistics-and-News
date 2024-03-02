import os

# Function to display worldwide responses between the given time range
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
            input_str = input("Enter starting month starting year ending month ending year (e.g., 4 2020 5 2022), or 'exit' to go back to the main menu: ")
            if input_str.lower() == 'exit':
                return None
            start_month, start_year, end_month, end_year = map(int, input_str.split())
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
        print("\n1. Enter time range")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            time_range = get_time_range()
            if time_range:
                start_month, start_year, end_month, end_year = time_range
                display_responses(start_month, start_year, end_month, end_year)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
