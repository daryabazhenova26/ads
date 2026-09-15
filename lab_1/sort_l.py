def min_dist(kms, tarifs):
    kms.sort()
    tarifs.sort(reverse=True)
    summa = 0
    for i in range(len(kms)):
        summa += kms[i]*tarifs[i]
    return summa


spisok_1 = list(map(int, input().split()))
spisok_2 = list(map(int, input().split()))
print(min_dist(spisok_1, spisok_2))

