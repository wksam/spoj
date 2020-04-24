import sys

for line in sys.stdin:
    if line.rstrip() == "42":
        break
    print(line.rstrip())