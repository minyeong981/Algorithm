'''
t초 동안 붕대 감으면서 1초마다 x 만큼 체력 회복
성공하면 y 체력 추가 회복
(현재 체력이 최대 체력보다 커질 순 없음)

'''
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