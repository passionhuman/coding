def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    edge = []
    V, E = map(int, input().split())
    for _ in range(E):
        s, e, w = map(int, input().split())
        edge.append([w,s,e])
    edge.sort()
    rep = [i for i in range(V+1)]
    cnt = 0
    total = 0
    for w,s,e in edge:
        if find_set(s) != find_set(e):
            cnt += 1
            union(s, e)
            total += w
            if cnt == V:
                break
    print(f'#{tc} {total}')