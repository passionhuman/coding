dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]
T=int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    stack = []
    black = white = 0
    arr = [[0] * (n) for _ in range(n)]
    arr[n // 2][n // 2 - 1] = arr[n // 2 - 1][n // 2] = 1
    arr[n // 2 - 1][n // 2 - 1] = arr[n // 2][n // 2] = 2
    for _ in range(m):
        c, r, color = map(int, input().split())
        r = r - 1
        c = c - 1
        arr[r][c] = color
        for d in range(8):
            check = True
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 0 and arr[nr][nc] != color:
                while check == True:
                    stack.append((nr,nc))
                    nr += dr[d]
                    nc += dc[d]
                    if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 0 and arr[nr][nc] != color:
                        pass
                    elif 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == color:
                        while stack:
                            a, b = stack.pop()
                            arr[a][b] = color
                            check = False
                    else:
                        stack = []
                        break

    for i in arr:
        for j in i:
            if j == 1:
                black += 1
            elif j == 2:
                white += 1

    print(f"#{test_case} {black} {white}")
