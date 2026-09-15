def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2

    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


N = int(input())
A = list(map(int, input().split()))

A = merge_sort(A)

print(*A)