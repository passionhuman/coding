T = int(input())
for tc in range(1, T + 1):
    n, m, L = map(int, input().split())
    ans = []
    heap = [0] * (n + 1)
    result = 0
    for i in range(m): # leaf 노드에 num 넣기
        leaf, num = map(int, input().split())
        heap[leaf] = num
        while True:
            temp = leaf // 2 # leaf 노드들의 부모노드에 다 넣기
            if temp == 0:
                break
            heap[temp] += num
            leaf = leaf // 2
    print(f'#{tc} {heap[L]}')