import sys
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

data = sys.stdin.read().split()
N = int(data[0])
x1, y1 = int(data[1]), int(data[2])
x2, y2 = int(data[3]), int(data[4])

moves = [(-2,-1), (-2,1), (-1,-2), (-1,2),
         (1,-2), (1,2), (2,-1), (2,1)]

start = (x1,y1)
end = (x2,y2)

queue = deque([start])
parents = {start: None}

while queue:
    x, y = queue.popleft()

    if (x,y) == end:        #дошли
        break

    for dx, dy in moves:
        nx, ny = x+dx, y+dy

        if 1 <= nx <= N and 1 <= ny <= N:
            if (nx, ny) not in parents:
                parents[(nx, ny)] = (x,y)
                queue.append((nx, ny))

path = []
cur = end
while cur is not None:
    path.append(cur)
    cur = parents[cur]

path.reverse()

print(len(path)-1)
for x, y in path:
    print(x, y)