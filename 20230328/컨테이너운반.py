T = int(input())
for tc in range(1, T + 1):
    c, t = map(int, input().split())
    con = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    con.sort()
    truck.sort()
    ans = 0
    while truck:
        temp = truck.pop()
        for i in range(len(con) - 1, -1, -1):
            if con[i] <= temp:
                ans += con.pop(i)
                break
    print(f'#{tc} {ans}')