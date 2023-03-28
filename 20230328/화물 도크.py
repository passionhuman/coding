t = int(input())
for tc in range(1, t+1):
    ans = 1
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key=lambda x: x[1])
    end_time = time.pop(0)[1]
    while time:
        s, e = time.pop(0)
        if end_time <= s:
            end_time = e
            ans += 1
    print(f'#{tc} {ans}')