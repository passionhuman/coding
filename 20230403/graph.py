from collections import deque
n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]
stack = []
visited = [0] * (n + 1)
dfs = []
for i in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
for i in range(len(adj)):
    adj[i] = sorted(adj[i])
visited[v] = 1
dfs.append(v)
while True:
    for i in adj[v]:
        if visited[i] == 0:
            stack.append(v)
            v = i
            visited[v] = 1
            dfs.append(v)
            break
    else:
        if stack:
            v = stack.pop()
        else:
            break

bfs = []
q = deque([])
visited = [0] * (n + 1)
visited[v] = 1
q.append(v)
bfs.append(v)
while q:
    size = len(q)
    for _ in range(size):
        v = q.popleft()
        for i in adj[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                bfs.append(i)
print(*dfs)
print(*bfs)