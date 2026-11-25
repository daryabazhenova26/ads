n, m = map(int, input().split())

mat = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    rebro = list(map(int, input().split()))
    mat[rebro[0]-1][rebro[1]-1] = 1
    mat[rebro[1]-1][rebro[0]-1] = 1

for i in range(n):
    if sum(mat[i]) < (len(mat[i]) - 1):
        print('NO')
        break
else:
    print('YES')