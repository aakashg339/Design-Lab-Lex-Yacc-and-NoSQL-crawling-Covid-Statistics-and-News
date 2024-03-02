import sys

current_key = None
current_value = []

# Read input from stdin
for line in sys.stdin:
    # Strip the line and split it into key and value
    parts = line.strip().split(' : ', 1)

    # If there are enough parts
    if len(parts) == 2:
        key, value = parts

        # If the key changes, it means we've moved on to the next key-value pair
        if key != current_key:
            # If there was a previous key, process its values
            if current_key is not None:
                # Combine all values for the current key
                combined_value = ' | '.join(current_value)
                # Output the combined key-value pair
                print(f'{current_key} : {combined_value}')
            
            # Update current key and reset the value list
            current_key = key
            current_value = []

        # Append the value to the list of values for the current key
        current_value.append(value)

# Process the last key-value pair
if current_key is not None:
    combined_value = ' | '.join(current_value)
    print(f'{current_key} : {combined_value}')
