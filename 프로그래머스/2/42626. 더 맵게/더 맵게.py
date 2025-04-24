import heapq
def solution(scoville, K):
    cnt = 0
    isFlag = False
    heapq.heapify(scoville)
    while len(scoville) > 1 :
        if scoville[0] >= K :
            return cnt
        
        v1 = heapq.heappop(scoville)
        v2 = heapq.heappop(scoville)
        heapq.heappush(scoville, (v1+(v2*2)))
        cnt += 1
    
    if scoville[0] >= K :
        return cnt
        
    return -1