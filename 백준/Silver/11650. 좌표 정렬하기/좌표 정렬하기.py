n = int(input())

dot = []
for _ in range(n):
    dot.append(list(map(int, input().split())))

# print(dot) [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]

dot.sort(key= lambda x : (x[0], x[1]))
# print(dot) [[1, -1], [1, 1], [2, 2], [3, 3], [3, 4]]

for result in dot :
    print(*result)