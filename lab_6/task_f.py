import sys
sys.setrecursionlimit(100_000)

def dfs(v):
    global cycle
    visited[v] = 'grey'
    for w in graph[v]:
        if visited[w] == 'white':
            dfs(w)
        if visited[w] == 'grey':
            cycle = True
    visited[v] = 'black'


N = int(input())
graph = dict()

for i in range(1, N+1):
    graph[i] = []

for i in range(1, N+1):
    dots = list(map(int, input().split()))
    graph[i] = [j + 1 for j in range(len(dots)) if dots[j] == 1]

visited = ['white']*(N+1)

cycle = False
for v in range(1, N+1):
    if visited[v] == 'white':
        dfs(v)
        if cycle:
            print(1)
            break
else:
    print(0)
