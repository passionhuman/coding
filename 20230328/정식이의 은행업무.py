import copy
t = int(input())
for tc in range(1, t+1):
    second = list(input())
    third = list(input())
    for s in range(len(second)):
        if second[s] == "0":
            second[s] = "1"

        elif second[s] == "1":
            second[s] = "0"

        for t in range(len(third)):
            if third[t] == "0":
                for temp in range(1,3):
                    third[t] = str(temp)
                    ans = 0
                    len_second = len(second)
                    for i in range(len(second)):
                        cnt = 2 ** (len_second - 1)
                        if cnt == 0:
                            cnt = 1
                        s_temp = int(second[i])
                        ans += cnt * s_temp
                        len_second -= 1
                    len_third = len(third)
                    ans2 = 0
                    for j in range(len(third)):
                        cnt2 = 3 ** (len_third - 1)
                        if cnt2 == 0:
                            cnt2 = 1
                        t_temp = int(third[j])
                        ans2 += cnt2 * t_temp
                        len_third -= 1

                    if ans == ans2:
                        st1 = copy.deepcopy(second)
                third[t] = "0"

            if third[t] == "1":
                for temp in range(3):
                    if temp == 1:
                        continue
                    third[t] = str(temp)
                    ans = 0
                    len_second = len(second)
                    for i in range(len(second)):
                        cnt = 2 ** (len_second - 1)
                        if cnt == 0:
                            cnt = 1
                        s_temp = int(second[i])
                        ans += cnt * s_temp
                        len_second -= 1
                    len_third = len(third)
                    ans2 = 0
                    for j in range(len(third)):
                        cnt2 = 3 ** (len_third - 1)
                        if cnt2 == 0:
                            cnt2 = 1
                        t_temp = int(third[j])
                        ans2 += cnt2 * t_temp
                        len_third -= 1

                    if ans == ans2:
                        st1 = copy.deepcopy(second)
                third[t] = "1"

            if third[t] == "2":
                for temp in range(2):
                    third[t] = str(temp)
                    ans = 0
                    len_second = len(second)
                    for i in range(len(second)):
                        cnt = 2 ** (len_second - 1)
                        if cnt == 0:
                            cnt = 1
                        s_temp = int(second[i])
                        ans += cnt * s_temp
                        len_second -= 1
                    len_third = len(third)
                    ans2 = 0
                    for j in range(len(third)):
                        cnt2 = 3 ** (len_third - 1)
                        if cnt2 == 0:
                            cnt2 = 1
                        t_temp = int(third[j])
                        ans2 += cnt2 * t_temp
                        len_third -= 1
                    if ans == ans2:
                        st1 = copy.deepcopy(second)
                third[t] = "2"

        if second[s] == "0":
            second[s] = "1"
        elif second[s] == "1":
            second[s] = "0"

    st_ans = 0
    len_st1 = len(st1)
    for i in range(len(st1)):
        cnt = 2 ** (len_st1 - 1)
        if cnt == 0:
            cnt = 1
        s_temp = int(st1[i])
        st_ans += cnt * s_temp
        len_st1 -= 1
    print(f"#{tc} {st_ans}")
