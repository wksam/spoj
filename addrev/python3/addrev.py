import sys

n = int(sys.stdin.readline())
for _ in range(int(n)):
    i, j = sys.stdin.readline().split(" ")
    k = int(i[::-1]) + int(j[::-1])
    sys.stdout.write(str(k).strip('0')[::-1] + '\n')