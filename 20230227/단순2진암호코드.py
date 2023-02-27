T = int(input())
pwd0 = [0,0,0,1,1,0,1]
pwd1 = [0,0,1,1,0,0,1]
pwd2 = [0,0,1,0,0,1,1]
pwd3 = [0,1,1,1,1,0,1]
pwd4 = [0,1,0,0,0,1,1]
pwd5 = [0,1,1,0,0,0,1]
pwd6 = [0,1,0,1,1,1,1]
pwd7 = [0,1,1,1,0,1,1]
pwd8 = [0,1,1,0,1,1,1]
pwd9 = [0,0,0,1,0,1,1]
for tc in range(1, T + 1):
    ans = []
    cnt = 0
    odd = 0
    even = 0
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(0, m, 7):
            if arr[i][j:j+7] == pwd0:
                ans.append(0)
                cnt += 1
            elif arr[i][j:j+7] == pwd1:
                ans.append(1)
                cnt += 1
            elif arr[i][j:j + 7] == pwd2:
                ans.append(2)
                cnt += 1
            elif arr[i][j:j+7] == pwd3:
                ans.append(3)
                cnt += 1
            elif arr[i][j:j+7] == pwd4:
                ans.append(4)
                cnt += 1
            elif arr[i][j:j+7] == pwd5:
                ans.append(5)
                cnt += 1
            elif arr[i][j:j+7] == pwd6:
                ans.append(6)
                cnt += 1
            elif arr[i][j:j+7] == pwd7:
                ans.append(7)
                cnt += 1
            elif arr[i][j:j+7] == pwd8:
                ans.append(8)
                cnt += 1
            elif arr[i][j:j+7] == pwd9:
                ans.append(9)
                cnt += 1
        if cnt == 8:
            break
    print(ans)
    for i in range(0, len(ans), 2):
        odd += 3 * ans[i]
    for i in range(1, len(ans), 2):
        even += ans[i]

    if (odd + even) % 10 == 0:
        print(f"#{tc} {sum(ans)}")
    else:
        print(f"#{tc} 0")