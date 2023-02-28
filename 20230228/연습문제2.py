hi = "0F97A3"

def solution(n):
    # n은 16진수 문자열
    # 길이 * 4 = 비트수
    l = len(n) * 4
    # 16진수 문자열을 숫자로 바꾸기
    x = int(n, 16)
    print(x)
    # 결과문자열
    result = ""
    # 뒤에서부터 7개씩 잘라서 2진수 만든뒤에 다시 10진수로 만들기
    for i in range(l-1, -1, -7):
        # 현재 위치 i에서 7개 잘라서 만든 이진수
        bin = ""
        # x의 i-j번째 비트 판별
        for j in range(7):
            # 음수만큼 쉬프트가 일어났다...
            # ==> 자리수가 넘어갔다
            if i - j < 0:
                break
            bin += "1" if x & (1 << i - j) else "0"

        print(bin, end = " ")
        dec = int(bin, 2) # 2진수 문자열을 10진수로 바꾸기
        result += str(dec) + " "
    print()
    print(result)
solution(hi)