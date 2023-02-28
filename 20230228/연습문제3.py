hi = "0269FAC9A0"
pass0 = "001101"
pass1 = "010011"
pass2 = "111011"
pass3 = "110001"
pass4 = "100011"
pass5 = "110111"
pass6 = "001011"
pass7 = "111101"
pass8 = "011001"
pass9 = "101111"
ans = []
def solution(n):
    global bin
    l = len(n) * 4
    x = int(n, 16)
    bin = ""
    for i in range(l-1,-1,-1):
        if x & (1 << i) != 0:
            bin += "1"
        else:
            bin += "0"
    print(bin)

solution(hi)
for i in range(len(bin)-1, -1,-1):
    if bin[i] == "1":
        c = i
        break
for i in range(c, -1, -6):
    if bin[i-5:i+1] == pass0:
        ans.append(0)
    elif bin[i-5:i+1] == pass1:
        ans.append(1)
    elif bin[i-5:i+1] == pass2:
        ans.append(2)
    elif bin[i-5:i+1] == pass3:
        ans.append(3)
    elif bin[i-5:i+1] == pass4:
        ans.append(4)
    elif bin[i-5:i+1] == pass5:
        ans.append(5)
    elif bin[i-5:i+1] == pass6:
        ans.append(6)
    elif bin[i-5:i+1] == pass7:
        ans.append(7)
    elif bin[i-5:i+1] == pass8:
        ans.append(8)
    elif bin[i-5:i+1] == pass9:
        ans.append(9)
ans = reversed(ans)

print(*ans)