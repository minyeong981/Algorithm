import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    
    for operation in operations :
        questtion, data = operation.split()
        data = int(data)
        
        if questtion == 'I' :
            heapq.heappush(max_heap, (-data, data))
            heapq.heappush(min_heap, data)
        elif questtion == 'D' :
            if max_heap and data == 1 :
                heapq.heappop(max_heap)
                min_heap.pop()
            elif min_heap and data == -1 :
                heapq.heappop(min_heap)
                max_heap.pop()
                
    if len(max_heap) == 0 :
        return [0, 0]
    
    return [max_heap[0][1], min_heap[0]]