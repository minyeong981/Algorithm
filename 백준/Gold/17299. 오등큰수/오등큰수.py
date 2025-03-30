from collections import Counter
import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
count = Counter(A)
#print(count) #Counter({1: 3, 2: 2, 3: 1, 4: 1})
NGF = [-1] * N
stack = []
for i in range(N) :
    while stack and count[A[stack[-1]]] < count[A[i]] :
        idx = stack.pop()
        NGF[idx] = A[i]
    stack.append(i)
print(*NGF)