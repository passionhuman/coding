t = int(input())
for tc in range(1, t+1):
    num, c = map(int, input().split())
    num = str(num)
    num_set = set([num])
    ans = set()

    for _ in range(c):
        while num_set:
            n = num_set.pop()
            n = list(n)
            for i in range(len(num)-1):
                for j in range(i+1, len(num)):
                    n[i], n[j] = n[j], n[i]
                    ans.add(''.join(n))
                    n[i], n[j] = n[j], n[i]
        num_set,ans = ans,num_set
    ans = max(map(int,num_set))
    print(f'#{tc} {ans}')