from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
elements = list(map(int, input().split()))
lst = deque(range(1,n+1))

#회전 횟수
cnt = 0

for target in elements:
    #목표 원소의 위치 찾기
    targetIndex = lst.index(target)

    if targetIndex <= len(lst)//2:
        # 왼쪽으로 회전
        lst.rotate(-targetIndex)
        cnt += targetIndex
    #오른쪽으로 회전
    else:
        lst.rotate(len(lst)-targetIndex)
        cnt += len(lst)-targetIndex

    #목표 원소 제거
    lst.popleft()

print(cnt)