from collections import deque
T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T + 1):
    n, m, r, c, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    q = deque([])
    visited = [[0] * m for _ in range(n)]
    q.append((r, c))
    visited[r][c] = 1
    cnt = 0
    time = 1
    while q:
        if time == L:
            break
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and arr[nr][nc] != 0:

                    if arr[r][c] == 2 and d in [2, 3]:
                        continue

                    elif arr[r][c] == 3 and d in [0, 1]:
                        continue

                    elif arr[r][c] == 4 and d in [1, 2]:
                        continue

                    elif arr[r][c] == 5 and d in [0, 2]:
                        continue

                    elif arr[r][c] == 6 and d in [0, 3]:
                        continue

                    elif arr[r][c] == 7 and d in [1, 3]:
                        continue

                    elif arr[nr][nc] == 2 and d in [2, 3]:
                        continue

                    elif arr[nr][nc] == 3 and d in [0, 1]:
                        continue

                    elif arr[nr][nc] == 4 and d in [0, 3]:
                        continue

                    elif arr[nr][nc] == 5 and d in [1, 3]:
                        continue

                    elif arr[nr][nc] == 6 and d in [1, 2]:
                        continue

                    elif arr[nr][nc] == 7 and d in [0, 2]:
                        continue

                    q.append((nr, nc))
                    visited[nr][nc] = 1

        time += 1
    for v in visited:
        for s in v:
            if s == 1:
                cnt += 1
    print(f'#{tc} {cnt}')

