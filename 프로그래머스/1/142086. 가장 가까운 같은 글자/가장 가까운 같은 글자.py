def solution(s):
    answer = []
    for i, ele1 in enumerate(s) :
        if ele1 not in s[:i] :
            answer.append(-1)
        else :
            cnt = 1
            for ele2 in s[i-1::-1] :
                if ele1 == ele2 :
                    answer.append(cnt)
                    break
                cnt += 1
            
    return answer