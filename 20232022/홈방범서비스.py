T = int(input())
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    q = deque([])
    max_home = 0
    for i in range(n):
        for j in range(n):
            for k in range(2 * n - 1):
                q.append((i,j))
                cnt = 0
                if city[i][j] == 1:
                    cnt += 1
                while q:
                    size = len(q)
                    for _ in range(size):
                        r, c = q.popleft()
                        if city[r][c] == 1:
                            cnt += 1
                        for d in range(4):
                            nr = r + dr[d] * k
                            nc = c + dr[d] * k
                            if 0 <= nr < n and 0 <= nc < n:
                                q.append((nr, nc))
                                if nr == r and nc == c:
                                    q = deque([])
                                    break
                if cnt * m >= (k+1) * (k+1) + k * k and cnt > max_home:
                    max_home = cnt
    print(max_home)