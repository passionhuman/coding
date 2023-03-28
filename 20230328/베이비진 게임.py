from collections import deque
t = int(input())
for tc in range(1, t+1):
    card = deque(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    babyjin1 = 0
    babyjin2 = 0
    check = 0
    while card:
        temp = card.popleft()
        p1[temp] += 1

        if babyjin2 != 1:
            for i in range(10):
                if p1[i] >= 3:
                    babyjin1 = 1
                    check = 1
                    break

            for i in range(8):
                if p1[i] >= 1:
                    if p1[i+1] >= 1:
                        if p1[i+2] >= 1:
                            babyjin1 = 1
                            check = 1
                            break


        if babyjin1 != 1:
            temp = card.popleft()
            p2[temp] += 1
            for i in range(10):
                if p2[i] >= 3:
                    babyjin2 = 1
                    check = 2
                    break

            for i in range(8):
                if p2[i] >= 1:
                    if p2[i+1] >= 1:
                        if p2[i+2] >= 1:
                            babyjin2 = 1
                            check = 2
                            break

    if check == 0:
        print(f'#{tc} 0')

    elif check == 1:
        print(f'#{tc} 1')

    else:
        print(f'#{tc} 2')