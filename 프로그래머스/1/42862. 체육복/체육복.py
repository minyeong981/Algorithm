def solution(n, lost, reserve):
    realLost = set(lost) - set(reserve)
    realReserve = set(reserve) - set(lost)
    
    for r in sorted(realReserve) :
        if r - 1 in realLost :
            realLost.remove(r - 1)
        elif r + 1 in realLost :
            realLost.remove(r + 1)
    
    return n - len(realLost)