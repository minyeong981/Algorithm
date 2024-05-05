import sys
input = sys.stdin.readline

n, k, t = map(int, input().split())
sharkList = list(map(int, input().split()))

sharkList.sort() # 상어 크기대로 정렬

stack = []
cnt = 0
i = 0
while cnt < k:
    if i < n and sharkList[i] < t:
        stack.append(sharkList[i])
        i += 1
    elif stack:
        t += stack.pop()
        cnt += 1
    else:
        break

print(t)
