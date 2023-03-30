def dfs(r,c,num):
    global min_num
    if min_num <= num:
        return

    elif r == n:
        if num < min_num:
            min_num = num
            return

    for j in range(n):
        if j not in v:
            v.append(j)
            dfs(r+1, j, num+arr[r][j])
            v.remove(j)


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    v = []
    min_num = 15 * 100
    dfs(0,0,0)
    print(f'#{tc} {min_num}')