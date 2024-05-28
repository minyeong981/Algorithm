import sys
input = sys.stdin.readline

n = int(input())
result = 0
length = len(str(n))

for i in range(1, length):
    result += i * (10**i - 10**(i-1)) # 숫자 범위별로 돌기

result += length * (n - 10**(length-1) + 1) # 마지막 자릿수에 해당하는 숫자들 별도로 계산해 더하기

print(result)
