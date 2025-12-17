def to_zpn(nmbr):
    stack = []
    zpn = []

    for ch in nmbr:
        if ch.isdigit():
            zpn.append(ch)

        elif ch == '+' or ch == '-':
            while stack and stack[-1] != '(':
                zpn.append(stack.pop())
            stack.append(ch)

        elif ch == '*' or ch == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                zpn.append(stack.pop())
            stack.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack[-1] != '(':
                zpn.append(stack.pop())
            stack.pop()

    while stack:
        zpn.append(stack.pop())

    return zpn


def calc(zpn):
    stack = []

    for x in zpn:
        if x.isdigit():
            stack.append(int(x))
        else:
            b = stack.pop()
            a = stack.pop()

            if x == '+':
                stack.append(a + b)
            if x == '-':
                stack.append(a - b)
            if x == '*':
                stack.append(a * b)
            if x == '/':
                stack.append(a / b)

    return stack[0]

nmbr = input("Enter an expression: ")

zpn = to_zpn(nmbr)
print("ZPN:", zpn)

res = calc(zpn)
print("Result:", res)
