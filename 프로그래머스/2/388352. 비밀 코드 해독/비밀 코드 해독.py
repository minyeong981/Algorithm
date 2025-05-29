from itertools import combinations
def solution(n, q, ans):
    answer = 0
    number = [i for i in range(1, n+1)]
    for combi in combinations(number, 5) :
        for i, question in enumerate(q) :
            if len(list(filter(lambda num: num in question, combi))) != ans[i] :
                break
        else :
            answer += 1
    return answer