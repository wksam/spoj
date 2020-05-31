import sys

n, k = sys.stdin.readline().split(" ")
count = 0
for _ in range(int(n)):
    t = int(sys.stdin.readline())
    if t % int(k) == 0:
        count += 1
sys.stdout.write(str(count))