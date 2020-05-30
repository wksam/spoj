n, k = input().split(" ")
count = 0
for _ in range(int(n)):
    t = int(input())
    if t % int(k) == 0:
        count += 1
print(count)