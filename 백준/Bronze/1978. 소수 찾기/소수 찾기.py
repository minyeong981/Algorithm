N = int(input())
A = list(input().split())

cnt = 0
for ele in A :
    newlst = []
    for num in range(1, int(ele)+1) :
        if int(ele)%num == 0:
            newlst.append(ele)
    if 1 < len(newlst) == 2:
        cnt +=1
print(cnt)