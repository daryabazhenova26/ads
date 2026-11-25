import sys
sys.setrecursionlimit(100_000)

def dfs(v, parent):
    global cycle
    visited[v] = 'grey'
    for w in graph[v]:
        if w == parent:
            continue        #игнорируем ребро в родителя
        if visited[w] == 'white':
            dfs(w, v)
        if visited[w] == 'grey':
            cycle = True
    visited[v] = 'black'

N, M = map(int, input().split())
graph = dict()

for i in range(1, N+1):
    graph[i] = []

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = ['white']*(N+1)
cycle = False

dfs(1, -1)      # -1 = заглушка для родителя

if not(cycle) and visited[1:].count('black') == N:
    print('YES')
else:
    print('NO')