def solution(n, times):
    left = 1
    right = max(times) * n  # 가장 오래 걸리는 경우
    answer = right
    
    while left <= right :
        mid = (left + right) // 2
        people = sum(mid // time for time in times) # mid 시간 동안 처리 가능한 사람의 수
        
        if people >= n :
            answer = mid
            right = mid - 1
        else :
            left = mid + 1
            
    return answer