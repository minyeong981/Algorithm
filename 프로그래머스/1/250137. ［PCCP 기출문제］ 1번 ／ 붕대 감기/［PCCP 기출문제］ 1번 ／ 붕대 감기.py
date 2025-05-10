def solution(bandage, health, attacks):
    answer = health
    lastTime = attacks[-1][0]
    currTime = flag = 0
    
    while currTime < lastTime :
        currTime += 1
        flag += 1
        
        
        for attack in attacks :
            if currTime == attack[0] :
                flag = 0
                answer = max(0, answer - attack[1])
                if not answer :
                    return -1

        
        if flag :
            if flag == bandage[0] :
                flag = 0
                answer = min(health, answer + bandage[2])
            answer = min(health, answer + bandage[1])  
        
    return answer
