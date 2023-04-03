t = int(input())

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x,y):
    p[find_set(y)] = find_set(x)

for tc in range(1, t+1):
    n, m = map(int, input().split())
    p = [i for i in range(n+1)]
    ans = set()

    st = list(map(int, input().split()))

    for i in range(m):
        union(st[i*2],st[i*2+1])
    print(p)

    for i in range(1, len(p)):
        ans.add(find_set(p[i]))
    print(f'#{tc} {len(ans)}')
