from collections import deque
import sys
input = sys.stdin.readline

def program(question) :
    if question[0] == 'push_back' :
        dq.append(question[1])
    elif question[0] == 'push_front' :
        dq.appendleft(question[1])
    elif question[0] == 'pop_front' :
        try :
            if dq[0]:
                print(dq.popleft())
        except :
            print(-1)
    elif question[0] == 'pop_back' :
        try :
            if dq[0] :
                print(dq.pop())
        except :
            print(-1)
    elif question[0] == 'size':
        print(len(dq))
    elif question[0] == 'empty':
        if len(dq) == 0 :
            print(1)
        else : print(0)
    elif question[0] == 'front':
        try :
            if  dq[0] : print(dq[0])
        except :
            print(-1)
    else :
        try :
            if dq[0]: print(dq[len(dq)-1])
        except :
            print(-1)



n = int(input())
dq = deque()
for _ in range(n):
    program(list(input().split()))