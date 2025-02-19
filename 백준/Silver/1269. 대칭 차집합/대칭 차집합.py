import sys
input = sys.stdin.readline

A, B = map(int, input().split())
ALst = list(map(int, input().split()))
BLst = list(map(int, input().split()))
union = set((*ALst, *BLst)) # 합집합 수
same = A + B - len(union)# 공통된 수 = 전체 수 - 합집합 수
# 대칭 차집합 = 전체 수 - 공통된 수
print(A + B - (same*2))