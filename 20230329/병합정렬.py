def mergesort(left,right):
    if left == right:
        return

    mid = (left+right) // 2
    mid -= 1

    mergesort(left,mid)

    mergesort(mid+1,right)
    mergesort(mid)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int,input().split()))
    mergesort(0, len(lst)-1)
