import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #수의 개수, 합 구해야 하는 횟수
num = list(map(int, input().split()))

sumV = [0]*(N+1) #누적합 계산
for i in range(1, N+1) :
    sumV[i] = sumV[i-1] + num[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(sumV[j] - sumV[i-1]) #j까지의 누적합에서 i-1까지의 누적합 빼기