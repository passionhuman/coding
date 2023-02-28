T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    r = c = n // 2
    ans = 0
    for i in range(n):
        for j in range(n):
            if  r >= abs(r - i) + abs(c - j):
                ans += int(arr[i][j])
    print(f"#{test_case} {ans}")