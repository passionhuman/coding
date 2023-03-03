T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    m = N//2
    for i in range(N):
        for j in range(abs(m-i), N-abs(m-i)):
            ans += arr[i][j]
    print(f'#{test_case} {ans}')