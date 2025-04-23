def solution(participant, completion):
    dic = {}
    for p in participant :
        if dic.get(p, 0) == 0 :
            dic[p] = 1
        else :
            dic[p] += 1
    for c in completion :
        if dic[c] > 0 :
            dic[c] -= 1
    for k, v in dic.items() :
        if v > 0 :
            return k
