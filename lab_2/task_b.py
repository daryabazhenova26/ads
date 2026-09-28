N, K = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

for elem in arr_2:
    left = -1
    right = len(arr_1)
    while (right - left) > 1:
        middle = (left+right)//2
        if arr_1[middle] > elem:
            right = middle
        else:
            left = middle
    if left == -1:
        print(arr_1[right])
    elif right == len(arr_1):
        print(arr_1[left])
    elif abs(arr_1[left]-elem) <= abs(arr_1[right]-elem):
        print(arr_1[left])
    else:
        print(arr_1[right])




