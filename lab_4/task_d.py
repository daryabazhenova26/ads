import heapq
import sys

heap = []

for s in sys.stdin:
    command = s.split()

    if command[0] == 'ADD':
        n = int(command[1])
        heapq.heappush(heap, -n)
    elif command[0] == 'EXTRACT':
        if heap:
            print(-heapq.heappop(heap))
        else:
            print('CANNOT')
    elif command[0] == 'CLEAR':
        heap.clear()