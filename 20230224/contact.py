for tc in range(1, 11):
    n, s = map(int, input().split())
    calling = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    q = []
    cnt = 1
    visited = [0] * 101
    ans = []
    for i in range(0, n, 2):
        adj[calling[i]].append(calling[i+1])
    q.append(s)
    visited[s] = 1
    while q:
        size = len(q)
        for _ in range(size):
            caller = q.pop(0)
            for c in adj[caller]:
                if visited[c] == 0:
                    q.append(c)
                    visited[c] = cnt
        cnt += 1

    for i in range(len(visited)):
        if visited[i] == max(visited):
            ans.append(i)
    print(f"#{tc} {max(ans)}")