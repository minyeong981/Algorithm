def calMinDist(mbti, dist):
    for i in range(4):
        if mbti[0][i] != mbti[1][i]:
            dist += 1
        if mbti[0][i] != mbti[2][i]:
            dist += 1
        if mbti[1][i] != mbti[2][i]:
            dist += 1
    return dist


from itertools import combinations

T = int(input())
for _ in range(T) :
    n = int(input())
    mbtiLst = list(input().split())

    minV = []
    if len(mbtiLst) >= 33 :
        dist = 0 # mbti 중 겹치는게 무조건 나옴
    else:
        for combi in combinations(mbtiLst, 3):
            minV.append(calMinDist(combi,0))
        dist = min(minV)

    print(dist)