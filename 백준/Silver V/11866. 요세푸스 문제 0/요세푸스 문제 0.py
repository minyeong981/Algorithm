from collections import deque
N, K = map(int, input().split())

line = deque()
killed = deque()
for person in range(1,N+1):
    line.append(str(person))
while line :
    for change in range(K-1) :
        line.append(line.popleft())
    killed.append(line.popleft())
    if line == False :
        break
print(f"<{', '.join(killed)}>")