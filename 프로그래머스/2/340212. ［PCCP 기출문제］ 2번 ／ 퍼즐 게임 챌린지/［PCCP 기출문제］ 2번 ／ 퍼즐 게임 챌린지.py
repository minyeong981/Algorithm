'''
현재 난이도 <= 내 숙련도 : time_cur만큼 시간 사용
현재 난이도 > 내 숙련도 : 퍼즐 총 (현재 난이도 - 내 숙련도)번 틀림
1) 퍼즐 틀릴 때마다 time_cur만큼 시간 사용
2) 추가로 time_prev만큼 시간을 사용해 전 퍼즐 다시 풀어야함
2-1) 다시 풀 때는 안 틀림
3) 퍼즐을 다 틀린 이후 다시 퍼즐 풀면 time_cur만큼 시간 사용해 퍼즐 해결
'''
def solution(diffs, times, limit):
    answer = limit
    n = len(diffs)
    minLevel = diffs[0]
    maxLevel = max(diffs)
    
    while minLevel <= maxLevel :
        mid = (minLevel + maxLevel) // 2
        totalTime = 0

        for i in range(n) :
            if diffs[i] <= mid :
                    totalTime += times[i]
            else :
                wrongCnt = diffs[i] - mid
                totalTime += (times[i] + times[i-1]) * wrongCnt + times[i]
        
        if totalTime > limit :
            minLevel = mid + 1
        else :
            answer = min(answer, mid)
            maxLevel = mid - 1
            
    return answer