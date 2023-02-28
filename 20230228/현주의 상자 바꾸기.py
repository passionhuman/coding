T = int(input())
for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    stack = [0] * (n+1)
    for i in range(q):
        left, right = map(int, input().split())
        for j in range(left, right+1):
            stack[j] = i + 1
    stack.pop(0)
    print(f'#{test_case}', *stack)