t = int(input())
for tc in range(1, t+1):
    num, c = list(map(int, input().split()))
    num = str(num)
    len_num = len(num)
    num = list(num)
    lst = [0] * len_num
    ans = []
    for i in range(len(num)):
        for j in range(i):
            if num[i] > num[j]:
                lst[i] += 1
    min_lst = min(lst)
    max_lst = max(lst)
    for i in range(c):
        num[max_lst], num[min_lst] = num[min_lst], num[max_lst]
        for i in range(min_lst+1):
            temp = num.pop(0)
            ans.append(temp)
        lst = [0] * len_num
        for i in range(len(num)):
            for j in range(i):
                if num[i] > num[j]:
                    lst[i] += 1
        min_lst = min(lst)
        max_lst = max(lst)
    print(f"#{tc}",''.join(ans + num))



