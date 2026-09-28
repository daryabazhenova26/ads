N, K = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

for elem in arr_2:
    left = -1
    right = len(arr_1)
    flag = False
    while (right - left) > 1:
        middle = (left+right)//2
        if arr_1[middle] == elem:
            flag = True
            break
        elif arr_1[middle] > elem:
            right = middle
        else:
            left = middle
    if flag:
        print('YES')
    else:
        print('NO')
