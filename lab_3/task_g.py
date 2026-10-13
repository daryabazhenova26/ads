n = int(input())
a = list(map(int, input().split()))

stek = []
need = 1

for wagon in a:
    stek.append(wagon)

    while stek and (stek[-1] == need):
        stek.pop()
        need += 1
if not stek:
    print('YES')
else:
    print('NO')