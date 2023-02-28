dr = [1, 0, 1, 1]
dc = [0, 1, 1, -1]
T =int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr =[list(map(str, input())) for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "o":
                for d in range(4):
                    cnt = 0
                    nr = i + dr[d]
                    nc = j + dc[d]
                    if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == "o":
                        while True:
                            cnt += 1
                            nr += dr[d]
                            nc += dc[d]
                            if nr < 0 or nr >= n or nc < 0 or nc >= n or arr[i][j] ==".":
                                break
                        if cnt >= 4:
                            check = True
    if check:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")