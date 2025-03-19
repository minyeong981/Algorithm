import bisect
import sys
input = sys.stdin.readline

n = int(input().rstrip())
portLst = list(map(int, input().split()))

connectLst = [portLst[0]]
for port in portLst :
    if connectLst[-1] < port :
        connectLst.append(port)
    else :
        i = bisect.bisect_left(connectLst, port)
        connectLst[i] = port

print(len(connectLst))