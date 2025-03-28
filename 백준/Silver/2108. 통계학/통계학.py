from collections import Counter
import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = []
for _ in range(N) :
    lst.append(int(input().rstrip()))

lst.sort()

count = Counter(lst)
maxFreq = max(count.values())
modeLst = []
for k, v in count.items() :
    if v == maxFreq :
        modeLst.append(k)
modeLst.sort()

print(round(sum(lst)/N))
print(lst[N//2])
print(modeLst[1] if len(modeLst) > 1 else modeLst[0])
print(lst[-1] - lst[0])