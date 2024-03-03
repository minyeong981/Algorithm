arr = [[0]*101 for _ in range(101)]
maxV = 0
for _ in range(4) :
    x1, y1, x2,y2 = map(int, input().split())
    maxV = max(x1, x2, y1, y2, maxV)

    for row in range(x1,x2):
        for col in range(y1, y2):
            arr[row][col] = 1

    cnt = 0
    for row in range(1,maxV+1):
        for col in range(1,maxV+1):
            if arr[row][col] == 1 :
                cnt+=1
print(cnt)