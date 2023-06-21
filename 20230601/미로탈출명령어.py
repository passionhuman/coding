def solution(n, m, x, y, r, c, k):
    # 이동할 수 없으면 impossible return
    # k = 1, (1,1) -> (5,1)
    distance = abs(r - x) + abs(c - y)
    if distance > k:
        return "impossible"
    if (k - distance) % 2:
        return "impossible"

    down = max(r - x, 0)
    left = max(y - c, 0)
    right = max(c - y, 0)
    up = max(x - r, 0)
    pair = (k - distance) // 2
    answer = ''
    for _ in range(k):
        if (down or pair) and x < n:
            answer += 'd'
            if down:
                down -= 1
            else:
                pair -= 1
                up += 1
            x += 1
        elif (left or pair) and y > 1:
            answer += 'l'
            if left:
                left -= 1
            else:
                pair -= 1
                right += 1
            y -= 1

        elif (right or pair) and y < m:
            answer += 'r'
            if right:
                right -= 1

            else:
                pair -= 1
                left += 1
            y += 1

        else:
            answer += 'u'
            if up:
                up -= 1
            else:
                pair -= 1
                down += 1
            x -= 1

    return answer


print(solution(3, 3, 1, 1, 2, 1 ,3))