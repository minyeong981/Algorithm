def sumtime(N, idx) :
    minsum = []
    sumV = 0
    for i in range(N) :
        sumV += idx[i][1]
        minsum.append(sumV)
    return sum(minsum)

# 0,0 > 1, 1
# 1,2 > 2, 3(1+2)
# 2,3 > 3, 6(3+3)

N = int(input())
time = [0]+list(map(int, input().split()))
idx = []


for i in range(1, N+1) :
    idx.append((i, time[i]))

idx.sort(key = lambda x:x[1])

result = sumtime(N, idx)
print(result)
