T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    cnt = 0

    # for j in range(m):
    #     if arr[0][j] != "W":
    #         cnt += 1
    # for j in range(m):
    #     if arr[n-1][j] != "R":
    #         cnt += 1
    #
    # for k in range(n-2):
    #     temp_cnt = cnt
    #     for i in range(1, n-1):
    #         for j in range(m):
    #             if arr[i][j] != "B":
    #                 cnt += 1

    for i in range(n):
        for j in range(m):
            for k in range()