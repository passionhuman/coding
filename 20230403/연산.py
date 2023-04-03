from collections import deque
def bfs(n):
    q = deque([])
    v = [0] * 1000001
    q.append(n)

    cnt = 0
    while q:
        size = len(q)
        for _ in range(size):
            c = q.popleft()
            if c == M:
                return cnt
            for d in (c+1, c-1, c*2 , c-10):
                if 0 <= d < 1000001 and v[d] == 0:
                    q.append(d)
                    v[d] = 1
        cnt += 1

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N)}')
