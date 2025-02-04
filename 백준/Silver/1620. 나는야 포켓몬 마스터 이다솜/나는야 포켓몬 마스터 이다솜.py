import sys
input = sys.stdin.readline

poNameList = {}
poNoList = {}
N, M = map(int, input().split())
for i in range(1, N+1) :
    poketmon = input().strip()
    poNameList[poketmon] = i
    poNoList[str(i)] = poketmon

for _ in range(M) :
    q = input().strip()
    if poNameList.get(q, -1) != -1 :
        print(poNameList.get(q))
    else :
        print(poNoList[q])
