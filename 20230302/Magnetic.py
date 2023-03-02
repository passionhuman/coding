for tc in range(1, 11):
    n = 100
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = [[] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i].append(arr[j][i])
    print(ans)