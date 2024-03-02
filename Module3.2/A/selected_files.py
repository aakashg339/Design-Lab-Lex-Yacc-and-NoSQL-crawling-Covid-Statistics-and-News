import os
import sys

def get_month_and_year(filename):
    parts = filename.split("_")
    year = int(parts[0])
    month = int(parts[1])
    return (year, month)

def get_files_in_time_range(start_month, start_year, end_month, end_year):
    start_date = (start_year, start_month)
    end_date = (end_year, end_month)
    
    files_in_range = []
    
    for file in os.listdir("Combined_txt"):
        if file.endswith(".txt"):
            file_date = get_month_and_year(file)
            if start_date <= file_date <= end_date:
                files_in_range.append(file)
    
    files_in_range.sort(key=get_month_and_year)  # Sort the list of files by month and year
    
    return files_in_range

def combine_txt_files(files_to_combine, output_file):
    with open(output_file, 'w') as outfile:
        for file in files_to_combine:
            with open(os.path.join("Combined_txt", file), 'r') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py start_month start_year end_month end_year")
        sys.exit(1)

    start_month, start_year, end_month, end_year = map(int, sys.argv[1:5])
    
    files_in_range = get_files_in_time_range(start_month, start_year, end_month, end_year)
    
    if files_in_range:
        for file in files_in_range:
            print(file)
        
        # Combine the contents of all selected text files into a single file
        output_file = "store.txt"
        combine_txt_files(files_in_range, output_file)
