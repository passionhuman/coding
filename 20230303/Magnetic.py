for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = [[] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            ans[i].append(arr[j][i])
    for i in range(n):
        for j in range(n):
            if ans[i][j] == 1:
                for k in range(j+1, n):
                    if ans[i][k] == 2:
                        cnt += 1
                        break
                    elif ans[i][k] == 1:
                        ans[i][k] = 0
    print(f"#{tc} {cnt}")