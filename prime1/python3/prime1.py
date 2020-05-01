t = input()
for i in range(int(t)):
    n = input().split(' ')
    low = int(n[0])
    high = int(n[1]) + 1

    for j in range(low, high):
        for k in range(2, j):
            if j % k == 0:
                break
        else:
            if(j > 1):
                print(j)