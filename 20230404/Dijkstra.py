'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
def dijkstra(s, V):
    U = [0] * (V+1) # U 최소비용이 결정된 정점 집합
    U[s] = 1
    for i in range(V+1): # s에서 나머지 정점
        D[i] = adjm[s][i]
    # while U! = V 남은 정점의 비용 결정
    N = V + 1 # N개의 정점
    for _ in range(N-1): # N-1개 정점의 비용 결정
        # D[w]가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]: # 남은 정점
                w = i
                minV = D[i]
        U[w] = 1
        # w에 인접인 정점에 대해, 기존비용 vs w를 거쳐가는 비용 비교
        for v in range(V+1):
            if 0 < adjm[w][v] < INF: # w에 인접인 v의 조건
                D[v] = min(D[v], D[w] + adjm[w][v])


INF = 10000
V, E = map(int, input().split())
adjm = [[INF] * (V+1) for _ in range(V+1)]
for i in range(V+1):
    adjm[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adjm[u][v] = w
D = [0] * (V+1)
dijkstra(0,V)
print(D)