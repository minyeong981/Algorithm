arr = [list(map(int, input().split())) for _ in range(9)]

maxV = 0
max_row = 0
max_col = 0
for row in range(9) :
    for col in range(9) :
        result = arr[row][col]
        if maxV < result :
            maxV = result
            max_row = row
            max_col = col

max_row += 1
max_col += 1

print(maxV)
print(max_row, max_col)