s = input()

stek = []
pairs = {')': '(', ']': '[', '}': '{'}
for bracket in s:
    if bracket in '([{':
        stek.append(bracket)
    else:
        if stek:
            if pairs[bracket] == stek[-1]:
                stek.pop()
            else:
                print('no')
                break
        else:
            print('no')
            break
else:
    if not stek:
        print('yes')
    else:
        print('no')