import sys
import math

t = sys.stdin.readline()
for i in range(int(t)):
    n = sys.stdin.readline().split(' ')
    low = int(n[0])
    high = int(n[1]) + 1

    for j in range(low, high):
        if j <= 1:
            continue
        if j == 2:
            print(j)
            continue
        if j > 2 and j % 2 == 0:
            continue

        max_div = math.floor(math.sqrt(j))
        for k in range(3, 1 + max_div, 2):
            if j % k == 0:
                break
        else:
            sys.stdout.write(str(j) + '\n')