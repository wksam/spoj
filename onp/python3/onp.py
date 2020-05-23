# 1. Priority of operators
# 2. No two operators of same priority can stay together in stack colomn
# 3. Lowest priority cannot be placed before highest priority
# 4. ( + ) Pop until find start bracket

t = input()
for t in range(int(t)):
    expression = list(input())
    stack = []
    rpn = ""
    
    for symbol in expression:
        if symbol.isalpha():
            rpn += symbol
        else:
            if symbol == ')':
                found = False
                while not found:
                    stackSymbol = stack.pop()
                    rpn += stackSymbol if stackSymbol != '(' else ''
                    found = stackSymbol == '('
            elif symbol == '^':
                stopPop = False
                while not stopPop:
                    if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '^':
                        rpn += stack.pop()
                    else:
                        stack.append(symbol)
                        stopPop = True
            elif symbol == '*' or symbol == '/':
                stopPop = False
                while not stopPop:
                    if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/':
                        rpn += stack.pop()
                    else:
                        stack.append(symbol)
                        stopPop = True
            elif symbol == '+' or symbol == '-':
                stopPop = False
                while not stopPop:
                    if stack[-1] == '+' or stack[-1] == '-':
                        rpn += stack.pop()
                    else:
                        stack.append(symbol)
                        stopPop = True
            else:
                stack.append(symbol)
    print(rpn)