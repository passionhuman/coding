T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    check = False
    for i in range(int(num ** (1/3)-1), int(num ** (1/3)) + 2):
        if i ** 3 == num:
            ans = i
            check = True
            break

    if check:
        print(f"#{tc} {ans}")
    else:
        print(f"#{tc} -1")