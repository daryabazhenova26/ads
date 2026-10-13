from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

dek = deque()


for i in range(n):
    while dek and (a[i] <= a[dek[-1]]):
        dek.pop()

    dek.append(i)
    while dek and (dek[0] < (i-k+1)):
        dek.popleft()
    if i >= (k-1):
        print(a[dek[0]])