T = int(input())
for tc in range(1, T + 1):
    n = float(input())
    b = ''
    cnt = 0
    while cnt < 13 and n != 0:
        n *= 2
        cnt += 1
        if n >= 1:
            n -= 1
            b += "1"
        else:
            b += "0"
    if cnt < 13:
        print(f'#{tc} {b}')
    else:
        print(f'#{tc} overflow')