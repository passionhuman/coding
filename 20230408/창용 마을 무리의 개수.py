t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    adj = [[] * (n + 1) for _ in range(n + 1)]
    v = [0] * (n + 1)
    temp = ans = 0
    for i in range(m):
        s, e = map(int, input().split())
        adj[s].append(e)
    q = []
    for i in range(len(adj)):
        temp += 1

        for j in range(len(adj[i])):
            q.append(adj[i][j])

        while q:
            if v[i] == 0:
                v[i] = temp
            num = q.pop(0)
            if v[num] == 0:
                v[num] = temp
                for k in range(len(adj[num])):
                    q.append(adj[num][k])

    for i in range(1, n + 1):
        if i in v:
            ans += 1

    for i in range(1,len(v)):
        if v[i] == 0:
            ans += 1

    print(f'#{tc} {ans}')
