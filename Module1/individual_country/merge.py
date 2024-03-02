import sys

with open('../Module1/individual_country/output_activecases.txt', 'r') as file1, \
     open('../Module1/individual_country/output_newcases.txt', 'r') as file2, \
     open('../Module1/individual_country/output_newdeaths.txt', 'r') as file3, \
     open('../Module1/individual_country/output_newrecoveries.txt', 'r') as file4:
    # Read the lines from each file
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    lines3 = file3.readlines()
    lines4 = file4.readlines()

country=sys.argv[1]
with open(f'../Module1/individual_country/merged_files/mfile_{country}.txt', 'w') as file:
    for line1, line2, line3, line4 in zip(lines1, lines2, lines3, lines4):
        merged_line = line1.strip() + line2.strip() + line3.strip() + line4.strip() + '\n'
        file.write(merged_line)