def check(start):
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            return False
    return True


n, m = map(int, input().split())
graph = {}

for i in range(1, n+1):
    graph[i] = []

for _ in range(1, m+1):
    u,v = map(int, input().split())
    graph[u].append(v)

perm = list(map(int, input().split()))
visited = [False]*(n+1)
rev_perm = reversed(perm)
for v in rev_perm:
    if not check(v):
        print('NO')
        break
else:
    print('YES')
