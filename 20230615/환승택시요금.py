def solution(n, s, a, b, fares):
    d = [[20000001 for _ in range(n+1)] for _ in range(n+1)]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x][y] = c
        d[y][x] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minV = 40000002
    for i in range(n):
        minV = min(minV, d[s][i]+d[i][a]+d[i][b])

    return minV

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
