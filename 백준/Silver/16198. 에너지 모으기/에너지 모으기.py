def cal(temp, sumV):
    if len(temp) == 2:
        result.append(sumV)
        return
    for i in range(1, len(temp) - 1):
        energy = temp[i - 1] * temp[i + 1]
        newTemp = temp[:i] + temp[i+1:]
        cal(newTemp, sumV + energy)

import sys
input = sys.stdin.readline

n = int(input())
beads = list(map(int, input().split()))
result = []

cal(beads, 0)
print(max(result))
