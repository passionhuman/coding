T = int(input())
pwd0 = [0, 0, 0, 1, 1, 0, 1]
pwd1 = [0, 0, 1, 1, 0, 0, 1]
pwd2 = [0, 0, 1, 0, 0, 1, 1]
pwd3 = [0, 1, 1, 1, 1, 0, 1]
pwd4 = [0, 1, 0, 0, 0, 1, 1]
pwd5 = [0, 1, 1, 0, 0, 0, 1]
pwd6 = [0, 1, 0, 1, 1, 1, 1]
pwd7 = [0, 1, 1, 1, 0, 1, 1]
pwd8 = [0, 1, 1, 0, 1, 1, 1]
pwd9 = [0, 0, 0, 1, 0, 1, 1]
for tc in range(1, T + 1):
    ans = []
    cnt = r = 0
    odd = 0
    even = 0
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        if r != 0:
            break
        for j in range(m - 1, -1, -1):
            if arr[i][j] == 1:
                r = i
                c = j
                break

    for k in range(c, 6, -7):
        if arr[r][k - 6:k + 1] == pwd0:
            ans.append(0)
        elif arr[r][k - 6:k + 1] == pwd1:
            ans.append(1)
        elif arr[r][k - 6:k + 1] == pwd2:
            ans.append(2)
        elif arr[r][k - 6:k + 1] == pwd3:
            ans.append(3)
        elif arr[r][k - 6:k + 1] == pwd4:
            ans.append(4)
        elif arr[r][k - 6:k + 1] == pwd5:
            ans.append(5)
        elif arr[r][k - 6:k + 1] == pwd6:
            ans.append(6)
        elif arr[r][k - 6:k + 1] == pwd7:
            ans.append(7)
        elif arr[r][k - 6:k + 1] == pwd8:
            ans.append(8)
        elif arr[r][k - 6:k + 1] == pwd9:
            ans.append(9)

    ans = ans[::-1]
    for i in range(0, len(ans), 2):
        odd += 3 * ans[i]
    for i in range(1, len(ans), 2):
        even += ans[i]

    if (odd + even) % 10 == 0:
        print(f"#{tc} {sum(ans)}")
    else:
        print(f"#{tc} 0")