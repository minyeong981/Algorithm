import sys
input = sys.stdin.readline

stack = []
N = int(input().strip())
for _ in range(N) :
    question = list(input().split())
    if question[0] == 'push' :
        stack.append(question[1])
    elif question[0] == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif question[0] == 'size' :
        print(len(stack))
    elif question[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    else :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
