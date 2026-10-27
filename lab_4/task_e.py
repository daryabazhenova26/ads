import heapq

N = int(input())
s = list(map(int, input().split()))

heap = []

for x in s:
    heapq.heappush(heap, x)

cost = 0

while N > 1:
    first_min_el = heapq.heappop(heap)
    second_min_el = heapq.heappop(heap)
    summa = first_min_el + second_min_el
    cost += 0.05*summa
    heapq.heappush(heap, summa)
    N -= 1

print(cost)