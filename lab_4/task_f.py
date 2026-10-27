import heapq


N = int(input())

cargo = []

for i in range(N):
    t, l = map(int, input().split())
    cargo.append((t, l))

cargo.sort()

heap = []

for t,l in cargo:
    if heap and heap[0] <= t:
        heapq.heappop(heap)
    heapq.heappush(heap, t+l)

print(len(heap))