from collections import deque

def bfs(g, start):
    n = len(g)
    dists = [float('inf')]*(n+1)
    dists[start] = 0

    parents = [-1]*(n+1)            #для восстановления пути

    Q = deque()
    Q.append(start)

    visited = [False]*(n+1)
    visited[start] = True

    while Q:
        cur = Q.popleft()
        for neighbour in g[cur]:
            if not visited[neighbour]:
                Q.append(neighbour)
                visited[neighbour] = True
                dists[neighbour] = dists[cur] + 1
                parents[neighbour] = cur
    return dists, parents



N = int(input())
graph = dict()

for i in range(1, N+1):
    graph[i] = []

for i in range(1, N+1):
    dots = list(map(int, input().split()))
    graph[i] = [j + 1 for j in range(len(dots)) if dots[j] == 1]

start, end = map(int, input().split())

distances, parents = bfs(graph, start)
L = distances[end]

if L == float('inf'):
    print(-1)
elif L == 0:
    print(0)
else:
    print(L)
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parents[cur]
    path.reverse()
    print(*path)



