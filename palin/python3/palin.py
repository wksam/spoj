testCase = input()
for t in range(int(testCase)):
    num = list(map(int, input()))
    n = len(num)
    
    all9 = all(x == 9 for x in num)
    if all9:
        print("1", end="")
        for i in range(1, n):
            print("0",end="")
        print("1")
    else:
        mid = int(n/2)
        indexOfEndOfLeftSide = mid - 1
        indexOfStartOfRightSide = mid + 1 if n % 2 else mid

        while indexOfEndOfLeftSide >= 0 and num[indexOfEndOfLeftSide] == num[indexOfStartOfRightSide]:
            indexOfEndOfLeftSide -= 1
            indexOfStartOfRightSide += 1
            
        leftSmaller = False
        if indexOfEndOfLeftSide < 0 or num[indexOfEndOfLeftSide] < num[indexOfStartOfRightSide]:
            leftSmaller = True

        while indexOfEndOfLeftSide >= 0:
            num[indexOfStartOfRightSide] = num[indexOfEndOfLeftSide]
            indexOfEndOfLeftSide -= 1
            indexOfStartOfRightSide += 1
        
        if leftSmaller:
            carry = 1
            indexOfEndOfLeftSide = mid - 1

            if n % 2 == 1:
                num[mid] += carry
                carry = int(num[mid] / 10)
                num[mid] %= 10
                indexOfStartOfRightSide = mid + 1
            else:
                indexOfStartOfRightSide = mid
            
            while indexOfEndOfLeftSide >= 0:
                num[indexOfEndOfLeftSide] += carry
                carry = int(num[indexOfEndOfLeftSide] / 10)
                num[indexOfEndOfLeftSide] %= 10
                num[indexOfStartOfRightSide] = num[indexOfEndOfLeftSide]
                indexOfEndOfLeftSide -= 1
                indexOfStartOfRightSide += 1

        for i in range(0, n):
            print(num[i], end="")
        print()