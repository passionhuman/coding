T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    bread_time = 0
    son_time = 0
    bread = 0
    check = True
    if 0 not in lst:
        while check == True:
            if son_time == max(lst):
                break
            bread_time += 1
            son_time += 1
            if M == bread_time:
                bread += K
                bread_time = 0

            for son in lst:
                if son_time == son:
                    if bread > 0:
                        bread -= 1
                    else:
                        check = False
                        break
    if 0 in lst:
        check = False
    if check:
        print(f"#{test_case} Possible")
    else:
        print(f"#{test_case} Impossible")