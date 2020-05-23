import math

t = input()
for t in range(int(t)):
    num = int(input())
    divsum = 1

    i = 2
    while i <= math.sqrt(num):
        if(num % i == 0):
            if(i == (num / i)):
                divsum += i
            else:
                divsum += int(i + num / i)
        i += 1
    print(divsum)