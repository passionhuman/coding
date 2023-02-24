from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    q = deque([])
    visited = [[0] * m for _ in range(n)]
    cnt = 1
    ans = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "W":
                q.append((i,j))
                visited[i][j] = -1
    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = cnt
        cnt += 1
    for i in range(n):
        for j in range(m):
            if visited[i][j] > 0:
                ans += visited[i][j]
    print(f'#{tc} {ans}')