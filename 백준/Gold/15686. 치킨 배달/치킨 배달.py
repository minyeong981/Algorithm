def solve(k, lst):
    global minV

    if len(lst) == M : #치킨집 리스트가 M개면
        totalDist = 0
        for r, c in house : #집 기준으로
            minDist = float('inf') #최소 거리
            for i, j in lst :
                dist = abs(r-i) + abs(c-j)
                minDist = min(dist, minDist)
            totalDist += minDist
        minV = min(totalDist, minV)


    if k == len(chicken):
        return

    solve(k+1, lst)
    solve(k+1, lst+[chicken[k]])

N, M = map(int, input().split())
street = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for r in range(N):
    for c in range(N):
        if street[r][c] == 2:       #2면 치킨집
            chicken.append((r, c))
        elif street[r][c] == 1:     #1이면 집
            house.append((r, c))

# print(chicken) #[(1, 2), (2, 2), (4, 4)]
# print(house)   #[(0, 2), (1, 4), (2, 1), (3, 2)]

minV = float('inf')
solve(0, [])
print(minV)
