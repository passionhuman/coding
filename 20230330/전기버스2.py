t = int(input())
for tc in range(1, t+1):
    n, *charge = list(map(int, input().split()))
    now = ans = back = 0
    c_lst = []
    go = charge[now]
    while True:
        before = now
        now += go
        if now >= len(charge):
            break
        temp = 0
        for i in range(go+before,before,-1):
            c_lst.append(charge[i]-temp)
            temp += 1
        go = max(c_lst)
        ans += 1
        c_lst = []
    print(f'#{tc} {ans}')