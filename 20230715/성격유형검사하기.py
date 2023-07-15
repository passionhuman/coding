def solution(survey, choices):
    answer = ''
    dict = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] == 1:
            dict[survey[i][0]] += 3
        elif choices[i] == 2:
            dict[survey[i][0]] += 2
        elif choices[i] == 3:
            dict[survey[i][0]] += 1
        elif choices[i] == 5:
            dict[survey[i][1]] += 1
        elif choices[i] == 6:
            dict[survey[i][1]] += 2
        elif choices[i] == 7:
            dict[survey[i][1]] += 3

    if dict["R"] > dict["T"]:
        answer += "R"
    elif dict["R"] < dict["T"]:
        answer += "T"
    elif dict["R"] == dict["T"]:
        answer += "R"

    if dict["C"] > dict["F"]:
        answer += "C"
    elif dict["C"] < dict["F"]:
        answer += "F"
    elif dict["C"] == dict["F"]:
        answer += "C"

    if dict["J"] > dict["M"]:
        answer += "J"
    elif dict["J"] < dict["M"]:
        answer += "M"
    elif dict["J"] == dict["M"]:
        answer += "J"

    if dict["A"] > dict["N"]:
        answer += "A"
    elif dict["A"] < dict["N"]:
        answer += "N"
    elif dict["A"] == dict["N"]:
        answer += "A"

    return answer

