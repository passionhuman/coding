def solution(today, terms, privacies):
    len_term = len(terms)
    dict = {}
    answer = []
    for term in terms:
        dict[term[0]] = term[2:]

    for i in range(len(privacies)):
        temp = int(dict[privacies[i][11]])

        year = int(today[0:4]) - (abs(temp) // 12)

        temp_month = int(today[5:7]) - abs(temp % 12)
        month = temp_month
        if temp_month <= 0:
            year -= 1
            month = 12 - abs(temp_month)

        day = int(today[-2:]) + 1

        print(year, month, day)

        if int(privacies[i][0:4]) < year:
            answer.append(i+1)
            continue

        elif int(privacies[i][0:4]) == year and month > int(privacies[i][5:7]):
            answer.append(i+1)
            continue

        elif int(privacies[i][0:4]) == year and month == int(privacies[i][5:7]) and day > int(privacies[i][8:10]):
            answer.append(i+1)
            continue

    return answer
