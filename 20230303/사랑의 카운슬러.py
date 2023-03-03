T = int(input())


def comb(i, k):
    global min_v
    if i == n:
        return

    if k == n // 2:
        # 가는 지렁이의 벡터합
        go = [0, 0]
        # 기다리는 지렁이의 벡터합
        wait = [0, 0]
        for j in range(n):
            if selected[j]:
                go[0] += worms[j][0]
                go[1] += worms[j][1]
            else:
                wait[0] += worms[j][0]
                wait[1] += worms[j][1]
        print(selected, k)
        print(go, wait)
        v_sum = (go[0] - wait[0]) ** 2 + (go[1] - wait[1]) ** 2
        if v_sum < min_v:
            min_v = v_sum
        return

    # i번째 지렁이를 고르고거나
    selected[i] = 1
    comb(i + 1, k + 1)
    # i번째 지렁이를 고르지 않거나
    selected[i] = 0
    comb(i + 1, k)


for tc in range(1, T + 1):
    n = int(input())

    worms = [list(map(int, input().split())) for _ in range(n)]
    selected = [0] * n
    min_v = (200000 * 2 * 20) ** 2

    comb(0, 0)

    print(f"#{tc} {min_v}")