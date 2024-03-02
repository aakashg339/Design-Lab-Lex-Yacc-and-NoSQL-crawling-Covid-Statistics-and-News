import os
import sys

for line in sys.stdin:

    words = line.strip().split(':')

    print(words)