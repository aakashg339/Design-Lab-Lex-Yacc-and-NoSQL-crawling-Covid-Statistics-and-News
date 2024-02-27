# Read data from file 1
with open('file1.txt', 'r') as file:
    file1_data = [line.strip().split(', ') for line in file]

# Read data from file 2
with open('file2.txt', 'r') as file:
    file2_data = [line.strip().split(', ') for line in file]

# Merge the rows based on the date
merged_data = {}
for row in file1_data + file2_data:
    date = row[0]
    if date not in merged_data:
        merged_data[date] = []
    merged_data[date].append(row[1:])

# Write merged data to a new file
with open('merged_file.txt', 'w') as file:
    for date, data in merged_data.items():
        for row_data in data:
            merged_row = [date] + row_data
            file.write(' '.join(merged_row) + '\n')
