def partiton(lst, l, r):
    p = lst[l]
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and lst[j] >= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[l], lst[j] = lst[j], lst[l]
    return j


def quicksort(lst, l, r):
    if l < r:
        s = partiton(lst, l, r)
        quicksort(lst, l, s-1)
        quicksort(lst, s+1, r)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    quicksort(lst, 0, n-1)
    print(f'#{tc} {lst[n//2]}')
