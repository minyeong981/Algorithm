def solution(s):
    answer = True
    
    stack = []
    for ele in s :
        if ele == '(' :
            stack.append(ele)
        else :
            if not len(stack) :
                answer = False
                break
            stack.pop()
    if len(stack) :
        answer = False
    return answer