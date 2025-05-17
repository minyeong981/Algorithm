def canPlace(x, y, size, park):
    n, m = len(park), len(park[0])
    if x + size > n or y + size > m:
        return False
    for i in range(size):
        for j in range(size):
            if park[x+i][y+j] != "-1":
                return False
    return True

def solution(mats, park):
    n, m = len(park), len(park[0])
    mats.sort(reverse=True)  # 큰 매트부터 시도
    for size in mats:
        for i in range(n):
            for j in range(m):
                if canPlace(i, j, size, park):
                    return size  # 가장 큰 것부터 찾으므로 바로 return
    return -1
