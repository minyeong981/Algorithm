n = ['N']+list(input())
# print(n)
cnt = 0
for i in range(1,len(n)):
    if n[i] == 'Y':
        for j in range(i, len(n), i):
            if n[j] == 'Y':
                n[j] = 'N'
            else :
                n[j] = 'Y'
        cnt += 1
if 'Y' in n :
    print(-1)
else :
    print(cnt)