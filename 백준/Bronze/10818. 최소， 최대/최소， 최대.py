N = int(input())
number = list(map(int, input().split()))
max =sorted(number)
print(max[0], max[-1])
