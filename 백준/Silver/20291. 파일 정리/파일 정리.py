import sys
input = sys.stdin.readline

N = int(input().strip())
dic = {}
for _ in range(N) :
    file = input().strip()
    i = file.index('.')
    if dic.get(file[i+1:], 0) :
        dic[file[i+1:]] += 1
    else :
        dic[file[i + 1:]] = 1
result = []
for key, value in dic.items() :
    result.append((key, value))

for name, cnt in sorted(result) :
    print(name, cnt)