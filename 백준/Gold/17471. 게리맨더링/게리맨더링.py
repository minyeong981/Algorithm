from itertools import combinations
from collections import deque

def connect(group):
    visited = [False] * (N+1)
    q = deque([list(group)[0]])  # 집합을 리스트로 변환하여 첫 번째 요소를 가져옴
    visited[list(group)[0]] = True
    count = 1

    while q:
        v = q.popleft()
        for w in G[v]:
            if w in group and not visited[w]:
                q.append(w)
                visited[w] = True
                count += 1

    return count == len(group)

def cal(group): # 인구 더하는 함수
    sumV = 0
    for i in group :
        sumV += people[i]
    return sumV

N = int(input())
people = [0] + list(map(int, input().split()))
G = {i: [] for i in range(1, N+1)} # 키: 구역 번호, 값: 인접 구역 번호

for i in range(1, N+1):
    data = list(map(int, input().split()))
    G[i] = data[1:]

minV = float('inf')

for j in range(1, N//2+1):
    for group1 in combinations(range(1, N+1), j): # 조합으로 구하기
        group1 = set(group1)
        group2 = set(range(1, N+1)) - group1

        if connect(group1) and connect(group2):
            result = abs(cal(group1) - cal(group2))
            minV = min(minV, result)

if minV == float('inf'): # 못 나누면 minV가 원래 값
    print(-1)
else:
    print(minV)
