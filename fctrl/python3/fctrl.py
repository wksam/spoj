import sys

t = sys.stdin.readline()
for _ in range(int(t)):
    n = int(sys.stdin.readline())
    count = 0
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5
    sys.stdout.write(str(count) + '\n')