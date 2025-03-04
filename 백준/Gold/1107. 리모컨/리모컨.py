import sys
input = sys.stdin.readline

def find(num) :
    if not wrong :
        return num

    possible = []

    for i in range(1000000) :
        if all(int(j) not in wrong for j in str(i)) :
            possible.append(i)

    if not possible :
         return 100

    return min(possible, key=lambda x : abs(x - num))



N = input().strip()
M = int(input().strip())

if M == 0:
    print(min(abs(int(N) - 100), len(N)))
    exit()

wrong = set(map(int, input().split()))

N = int(N)
closest = find(N)
cnt = len(str(closest)) + abs(closest - N)
print(min(abs(N - 100), cnt))

