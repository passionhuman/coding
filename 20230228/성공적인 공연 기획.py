T = int(input())
for test_case in range(1, T + 1):
    sit = []
    result = 0
    n = input()
    ans = int(n[0])
    for i in range(1, len(n)):
        if n[i] != "0":
            if ans >= i:
                pass
            else:
                result += i - ans
                temp = i - ans
                ans += temp
        ans += int(n[i])
    print(f"#{test_case} {result}")