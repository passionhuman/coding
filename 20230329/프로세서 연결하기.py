dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r,c):
    global cnt
    cnt += 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            v[nr][nc] = cnt
            while True:
                nr = dr[d]
                nc = dc[d]
                if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
                    pass
                elif 0 >=



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = []
    cnt = 1
    v = [[0] * n for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, n-1):
           if arr[i][j] == 1:
               lst.append((i,j))
    a, b = lst[0]
    bfs(a,b)

