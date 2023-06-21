def solution(n, m, x, y, r, c, k):
    answer = ''
    distance = abs(r - x) + abs(c - y)
    if (k - distance) < 0:
        return "impossible"
    if (k - distance) % 2 == 1:
        return "impossible"
    up = down = left = right = 0
    if x > r:
        up = x - r
    elif x < r:
        down = r - x

    if y > c:
        left = y - c
    elif y < c:
        right = c - y

    answer += (down * "d")
    answer += (left * "l")
    answer += (right * "r")
    answer += (up * "u")

    move = (k - distance) // 2

    for _ in range(move):
        if r+1 <= n:
            answer += "du"

        elif c-1 >= 1:
            answer += "lr"

        else:
            answer += "rl"
    return answer

print(solution(2, 2, 0, 0, 1, 0, 3))