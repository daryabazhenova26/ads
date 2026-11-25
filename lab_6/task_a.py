n = int(input())

mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

flag = True
for i in range(n):
    for j in range(n):
        if (mat[i][j] != mat[j][i]) or (i==j and mat[i][j] != 0):
            print('NO')
            flag = False
            break
    if not flag:
        break
if flag:
    print('YES')

