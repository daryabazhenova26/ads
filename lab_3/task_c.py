exp = input().split()
stek = []

for el in exp:
    if el not in '+-*':
        stek.append(int(el))
    else:
        b = stek.pop()
        a = stek.pop()
        if el == '+':
            result = a + b
        elif el == '-':
            result = a - b
        elif el == '*':
            result = a*b
        stek.append(result)
print(stek.pop())