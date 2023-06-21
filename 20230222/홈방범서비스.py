T = int(input())
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    q = deque([])
    q2 = deque([])
    max_home = 0
    ans = []
    for i in range(n):
        for j in range(n):
            visited = [[0] * n for _ in range(n)]
            visited[i][j] = 1
            cnt = 0
            q.append((i, j))
            for k in range(n * 2 - 1):
                while q:
                    size = len(q)
                    r, c = q.popleft()
                    if city[r][c] == 1:
                        cnt += 1
                    for _ in range(size):
                        for d in range(4):
                            nr = r + dr[d]
                            nc = c + dc[d]
                            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                                q2.append((nr, nc))
                                visited[nr][nc] = 1

                if cnt * m >= (k + 1) * (k + 1) + k * k and cnt > max_home:
                    max_home = cnt
                q = q2
                q2 = deque([])

    print(f'#{tc} {max_home}')
