T =int(input())
dr = [1, 0, 1, 1]
dc = [0, 1, 1, -1]
for tc in range(1, T + 1):
    n = int(input())
    check = False
    arr =[list(map(str, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "o":
                for d in range(4):
                    cnt = 1
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == "o":
                        while True:
                            cnt += 1
                            nr += dr[d]
                            nc += dc[d]
                            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == "o":
                                pass
                            else:
                                break
                        if cnt >= 5:
                            check = True
    if check:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")