import sys

stop = False
for line in sys.stdin:
    if line.rstrip() == "42":
        stop = True
    if not stop:
        print(line.rstrip())