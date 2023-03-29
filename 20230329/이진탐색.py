def binary(s,e,t):
    global ans
    global check
    while s <= e:
        mid = (s + e) // 2
        if n_lst[mid] == t:
            ans += 1
            return

        elif n_lst[mid] < t:
            if check == 1:
                return
            s = mid + 1
            check = 1

        elif n_lst[mid] > t:
            if check == 2:
                return
            e = mid - 1
            check = 2

t = int(input())
for tc in range(1, t+1):
    ans = 0
    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))
    n_lst = sorted(n_lst)
    m_lst = list(map(int, input().split()))
    for i in range(len(m_lst)):
        check = 0
        binary(0,len(n_lst)-1,m_lst[i])
    print(f'#{tc} {ans}')

