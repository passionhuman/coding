def promising(i, j):
    for di, dj in [[-1,-1],[-1,0],[-1,1]]:
        ni, nj = i+di, j+dj
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:
                return 0
            ni, nj = ni+di, nj+dj
    return 1

def f(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if promising(i, j):
                board[i][j] = 1
                f(i+1, N)
                board[i][j] = 0

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    cnt = 0
    f(0, N)
    print(f"#{tc} {cnt}")