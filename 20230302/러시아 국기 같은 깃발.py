T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    white = 0
    ans = 2500
    for i in range(0, n-2):
        for w in arr[i]:
            if w != "W":
                white += 1
        Blue = 0
        for j in range(i+1, n-1):
            for b in arr[j]:
                if b != "B":
                    Blue += 1
            Red = 0
            for k in range(j+1, n):
                for r in arr[k]:
                    if r != "R":
                        Red += 1
            if white + Blue + Red < ans:
                ans = white + Blue + Red
    print(f'#{test_case} {ans}')
