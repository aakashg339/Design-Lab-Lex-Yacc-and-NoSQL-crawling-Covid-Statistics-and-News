import sys

for line in sys.stdin:
    if line.count(':') == 1:
        key, value = line.strip().rsplit(':', 1)
        if key.split()[0][0].isdigit():
            key = key.split(':', 1)[-1]
        print(f'{key.strip()} : {value.strip()}')
