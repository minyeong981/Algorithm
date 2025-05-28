def solution(n, w, num):
    answer = 0
    boxes = [i for i in range(1, w*(n//w+1)+1)]
    warehouse = []
    floor = 0
    for i in range(0, n, w) :
        if floor % 2 :
            warehouse.append(boxes[i+w-1:i-1:-1])
        else :
            warehouse.append(boxes[i:i+w])
        floor += 1
    
    print(warehouse)
    
    for line in warehouse :
        if num in line :
            numIndex = line.index(num)
            if warehouse[-1][numIndex] > n :
                return len(warehouse) - answer -1
            break
        answer += 1
    return len(warehouse) - answer
    