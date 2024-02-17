import sys
from collections import deque

dq = deque()
def get_input() :
    return sys.stdin.readline().strip()

N = int(input())

for tc in range(N):
    question = get_input()

    if question[0] == '1':
        dq.appendleft(question[2:])
    elif question[0] == '2':
        dq.append(question[2:])
    elif question[0] == '3':
        print(dq.popleft() if dq else -1)
    elif question[0] == '4':
        print(dq.pop() if dq else -1)
    elif question[0] == '5':
        print(len(dq))
    elif question[0] == '6':
        print(0 if dq else 1)
    elif question[0] == '7' :
        print(dq[0] if dq else -1)
    elif question[0] == '8' :
        print(dq[-1] if dq else -1)