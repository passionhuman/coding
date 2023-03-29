def merge(left,right):
    pass
def msort(s,e):
    if s == e:
        return

    m = (s+e) // 2
    msort(s,m)
    msort(m+1,e)
    k = 0
    l, r = s, m+1
    while l <= m or r <= e:
        if l<=m and r<=e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    msort(arr)