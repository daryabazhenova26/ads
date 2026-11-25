n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

istoki = []
stoki = []

for i in range(n):
    sum_str = 0
    sum_col = 0

    for j in range(n):
        sum_col += mat[j][i]
        sum_str += mat[i][j]
    if sum_str != 0:
        if sum_col == 0:
            istoki.append(i + 1)
    else:
        stoki.append(i + 1)
        if sum_col == 0:
            istoki.append(i + 1)

print(len(istoki))
print(*istoki, sep='\n')
print(len(stoki))
print(*stoki, sep='\n')
