import sys
sys.setrecursionlimit(200000)

def dfs(start, comp):
    visited[start] = 'grey'
    comp.append(start)
    for v in graph[start]:
        if visited[v] == 'white':
            dfs(v, comp)
    visited[start] ='black'


N, M = map(int, input().split())
graph = dict()

for i in range(1, N+1):
    graph[i] = []
for i in range(M):
    rebro = list(map(int, input().split()))
    graph[rebro[0]].append(rebro[1])
    graph[rebro[1]].append(rebro[0])

visited = ['white']*(N+1)
comps = []

for i in range(1, N+1):
    if visited[i] == 'white':
        cur_comp = []
        dfs(i, cur_comp)
        comps.append(cur_comp)


print(len(comps))
for i in range(len(comps)):
    print(len(comps[i]))
    print(*comps[i])

