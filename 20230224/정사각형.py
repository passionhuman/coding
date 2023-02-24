dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    q = []
    start = 0
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            q.append((i,j))
            cnt = 1
            while q:
                r, c = q.pop(0)
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < n and board[r][c] + 1 == board[nr][nc]:
                        q.append((nr, nc))
                        cnt += 1

                    if cnt > max_cnt:
                        max_cnt = cnt
                        start = board[i][j]

                    elif cnt == max_cnt and board[i][j] < start:
                        start = board[i][j]

    print(f'#{tc} {start} {max_cnt}')