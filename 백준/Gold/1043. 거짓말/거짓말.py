import sys
input = sys.stdin.readline

def checkedFact(fact) :
    if fact[0] > 0:  # 진실을 안다면
        for ele in fact[1:]:
            truePeople.add(ele)
        return len(truePeople)

    else:
        print(M)
        exit()


N, M = map(int, input().split())
fact = list(map(int, input().split()))

parties = [list(map(int, input().split())) for _ in range(M)]
checked = [True] * (M + 1)
truePeople = set()
preCnt = currCnt = checkedFact(fact)

i = 0
while i <= M :
    if i == 0 :
        for party in parties :
            i += 1
            if checked[i] :
                if truePeople.intersection(party[1:]) :
                    currCnt = checkedFact(party)
                    checked[i] = False
            # print('preCnt : ', preCnt, 'currCnt : ', currCnt, checked)
            if preCnt != currCnt :
                i = 0
                preCnt = currCnt
                break
            if i == M :
                print(checked.count(True) - 1)
                exit()