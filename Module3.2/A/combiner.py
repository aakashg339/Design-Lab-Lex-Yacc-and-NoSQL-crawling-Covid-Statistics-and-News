import sys

current_key = None
current_values = []

for line in sys.stdin:
    key, value = line.strip().split(':', 1)
    
    if current_key == key:
        current_values.append(value.strip())
    else:
        if current_key:
            combined_values = ', '.join(current_values)
            print(f'{current_key.strip()} : {combined_values}')
        
        current_key = key
        current_values = [value.strip()]

# Output the last key-value pair
if current_key:
    combined_values = ', '.join(current_values)
    print(f'{current_key.strip()} : {combined_values}')
