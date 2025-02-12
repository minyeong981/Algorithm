import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

# 1. 양수, 1, 0, 음수로 나누어 정렬
pos = []
neg = []
zero = 0
one = 0

for num in lst:
    if num > 1:
        pos.append(num)
    elif num == 1:
        one += 1  # 1은 묶지 않고 더하는 게 이득
    elif num == 0:
        zero += 1
    else:
        neg.append(num)

# 2. 양수는 내림차순 정렬 (큰 것끼리 곱해야 최댓값)
pos.sort(reverse=True)

# 3. 음수는 오름차순 정렬 (작은 것끼리 곱해야 최댓값)
neg.sort()

# 4. 양수 계산
result = 0
while len(pos) > 1:
    result += pos.pop(0) * pos.pop(0)
if pos:
    result += pos[0]

# 5. 음수 계산
while len(neg) > 1:
    result += neg.pop(0) * neg.pop(0)

# 6. 남은 음수가 하나 있고 0이 있다면, 곱해서 0으로 만들기
if neg:
    if zero == 0:
        result += neg[0]  # 0이 없으면 그냥 더함

# 7. 1은 무조건 더하기
result += one

print(result)