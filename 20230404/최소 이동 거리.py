def dijkstra(s, V):
    U = [0] * (V + 1)
    U[s] = 1
    D[s] = 0

    for e, w in adjl[s]:
        D[e] = w

    for _ in range(V):
        minV = 11
        t = 0
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
        U[t] = 1
        for e, w in adjl[t]:
            D[e] = min(D[e], D[t] + w)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjl[s].append([e, w])

    D = [11] * (V + 1)
    dijkstra(0, V)
    print(f'#{tc} {D[-1]}')