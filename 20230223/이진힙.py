# 최대 100개의 key
# 최대힙
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return

T = int(input())
for tc in range(1, T + 1):
    heap = [0] * 501
    last = 0
    n = int(input())
    num = list(map(int, input().split()))
    ans = []
    start = n
    result = 0
    for e in num:
        enq(e)
    while True:
        next = start // 2
        ans.append(heap[next])
        start = next
        if next == 0:
            break
    for a in ans:
        result += a

    print(f"#{tc} {result}")