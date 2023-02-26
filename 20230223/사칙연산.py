def postorder(t):
    if t:
        postorder(lchild[t])
        postorder(rchild[t])
        if heap[t] == "+":
            heap[t] = int(heap[lchild[t]]) + int(heap[rchild[t]])
        elif heap[t] == "-":
            heap[t] = int(heap[lchild[t]]) - int(heap[rchild[t]])
        elif heap[t] == "*":
            heap[t] = int(heap[lchild[t]]) * int(heap[rchild[t]])
        elif heap[t] == "/":
            heap[t] = int(heap[lchild[t]]) // int(heap[rchild[t]])

for tc in range(1, 11):
    n = int(input())
    ans = []
    heap = [0] * (n + 1)
    lchild = [0] * (n + 1)
    rchild = [0] * (n + 1)
    result = 0
    for i in range(n):
        lst = input().split()
        if len(lst) == 4:
            heap[int(lst[0])] = lst[1]
            lchild[int(lst[0])] = int(lst[2])
            rchild[int(lst[0])] = int(lst[3])

        else:
            heap[int(lst[0])] = int(lst[1])
    postorder(1)

    print(f'#{tc} {heap[1]}')