def dfs(start):
    visited[start] = 'grey'
    for v in graph[start]:
        if visited[v] == 'white':
            dfs(v)
    visited[start] ='black'


N, S = map(int, input().split())
graph = {}
for i in range(1, N+1):
    dots = list(map(int, input().split()))
    graph[i] = [j+1 for j in range(len(dots)) if dots[j] == 1]

visited = ['white']*(N+1)

dfs(S)
print(len(visited)-visited.count('white'))