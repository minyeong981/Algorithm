import sys
input = sys.stdin.readline

S = input().strip()
lst = set()
i, j = 0, 1
while i <= j and i <= len(S) and j <= len(S):
    lst.add(S[i:j])
    if j == len(S) :
        i += 1
        j = i
    j += 1

print(len(lst))