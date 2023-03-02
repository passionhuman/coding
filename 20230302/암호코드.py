decrypt = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # 중복 체크
    dup_check = []
    # 결과, 답
    result = 0

    # 각 줄에 대해서 중복 처리 하기
    arr = list(set([input()[:m] for _ in range(n)]))

    # 각 줄에서 코드 검사
    for i in range(len(arr)):
        # 한 줄 가져오기
        row = arr[i]

        # 16진수 문자열 => 숫자 => 이진수 문자열
        bin_row = ""
        for c in row:
            # 글자 하나 떼서 검사
            c_hex = int(c, 16)
            # 16진수는 이진수 * 4, 4번 비교
            for j in range(3, -1, -1):
                bin_row += "1" if c_hex & (1 << j) else "0"

        # 이진수 문자열로 바꿨는데 그안에 1이 없다???
        if "1" not in bin_row:
            # 다음 줄 검사
            continue
        else:
            # 0 과 1 의 비율
            ratio = [0] * 4
            # 0 1 0 1 순서로 번갈아 가면서 나온다.
            # 모든코드는 마지막이 1로 끝나니까 전체줄의 오른쪽 0은 모두 제거
            bin_row = bin_row.rstrip("0")

            new_code = []
            # 코드의 맨끝이 1이니까 뒤부터 비율을 세준다.
            for j in range(len(bin_row) - 1, -1, -1):
                # 마지막 1의 개수 세기
                if bin_row[j] == "1" and ratio[2] == 0:
                    ratio[3] += 1
                # 세번째 0의 개수 세기
                elif bin_row[j] == "0" and ratio[1] == 0:
                    ratio[2] += 1
                # 두번째 1의 개수 세기
                elif bin_row[j] == "1" and ratio[0] == 0:
                    ratio[1] += 1
                elif bin_row[j] == "0" and bin_row[j - 1] == "1":
                    # 첫번째 0을 제외한 이진수들의 숫자를 모두 셌으니
                    # 비율계산 시작
                    # 같은비율로 늘어나니까 제일 작은수를 구해서 나눠버리면
                    min_ratio = min(ratio[1:4])
                    number = decrypt[(ratio[1] // min_ratio, ratio[2] // min_ratio, ratio[3] // min_ratio)]
                    # 비율 계산 다했고, 한줄에 코드뭉치가 여러개 있을수도 있으니까 비율 초기화
                    ratio = [0] * 4
                    # 코드에 해당하는 숫자를 구해서 새로운 코드를 만들면 된다.
                    # 뒤부터 만들었다는것 조심
                    new_code.append(number)
                    # 현재 만든 코드의 길이가 8이면
                    if len(new_code) == 8:
                        # 검증코드 계산
                        odd = new_code[1] + new_code[3] + new_code[5] + new_code[7]
                        even = new_code[0] + new_code[2] + new_code[4] + new_code[6]
                        # 계산 결과를 10으로 나누어서 떨어지면 올바른 코드
                        if (odd * 3 + even) % 10 == 0 and new_code not in dup_check:
                            # 각 자리수를 더해서 저장
                            result += odd + even
                            # 중복 처리
                            dup_check.append(new_code)
                        new_code = []  # 한줄에 다른 코드뭉치 있을수도 있으니 초기화
    print(f"#{tc} {result}")