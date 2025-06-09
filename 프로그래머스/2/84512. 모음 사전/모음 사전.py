def solution(word):
    answer = 0
    aeiou_dict = { 
        'A' : 0, 
        'E' : 1,
        'I' : 2,
        'O' : 3,
        'U' : 4
    }
    weights = [pow(5, i) for i in range(5)][::-1]

    for i, alphabet in enumerate(word) :
        answer += aeiou_dict[alphabet] * sum(weights[i:]) + 1
    return answer