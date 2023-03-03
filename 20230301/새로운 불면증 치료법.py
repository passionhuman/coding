T = int(input())
for test_case in range(1, T + 1):
    cnt = [0] * 10
    counting = 0
    n = input()
    result = n
    multiple = 1
    while True:
        result = int(n) * multiple
        result = str(result)
        for i in range(len(result)):
            temp = int(result[i])
            cnt[temp] = 1

        for i in cnt:
            if i == 1:
                pass
            else:
                break
        else:
            break
        multiple += 1
        counting += 1
    print(f"#{test_case} {result}")