from itertools import permutations

def same(user, banned_id):
    for word in range(len(user)):
        if len(user[word]) != len(banned_id[word]):  #
            return False
        for alpha in range(len(banned_id[word])):
            if banned_id[word][alpha] == '*' or user[word][alpha] == banned_id[word][alpha]:
                continue
            else:
                return False
    return True

def solution(user_id, banned_id):
    user_per = list(permutations(user_id, len(banned_id)))
    banned_list = []

    for user in user_per:
        if same(user, banned_id):
            T = set(user)
            if T not in banned_list:
                banned_list.append(T)
        else:
            continue
    return len(banned_list)