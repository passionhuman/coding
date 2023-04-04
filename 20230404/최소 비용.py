from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs(r,c):
    global v
    q = deque([(0,0)])
    v = [[0] * N for _ in range(N)]
    v[r][c] = 0
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:

                if v[nr][nc] == 0:
                    v[nr][nc] = v[r][c] + 1  + max(arr[nr][nc] - arr[r][c],0)
                    q.append((nr,nc))

                if v[nr][nc] != 0:
                    temp = v[r][c] + 1 + max(arr[nr][nc] - arr[r][c],0)
                    if v[nr][nc] > temp:
                        v[nr][nc] = temp
                        q.append((nr,nc))
    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bfs(0,0)
    print(f'#{tc} {v[N-1][N-1]}')
