import sys
input = sys.stdin.readline

N, C = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

# 조합 1개
for weight in weights :
    if weight == C :
        print(1)
        exit()

# 조합 2개 (투 포인터)
for i in range(N) :
    target = C - weights[i]
    left, right = i+1, N-1

    while left <= right :
        mid = (left + right) // 2
        if weights[mid] == target :
            print(1)
            exit()
        elif weights[mid] < target :
            left = mid + 1
        else :
            right = mid - 1

# 조합 3개
for i in range(N) :
    for j in range(i+1, N):
        target = C - (weights[i] + weights[j])
        if target < 0 : # 더해야할 값이 0보다 작으면 안 봐도 됨
            continue
        left, right = j + 1, N - 1

        while left <= right:
            mid = (left + right) // 2
            if weights[mid] == target:
                print(1)
                exit()
            elif weights[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

print(0)