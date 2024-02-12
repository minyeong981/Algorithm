import sys
stack = []

N = int(input())
for n in range(N) :
    questions = list(map(int, sys.stdin.readline().split()))

    if questions[0] == 1:
        stack.append(questions[1])
    elif questions[0] == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif questions[0] == 3:
        print(len(stack))
    elif questions[0] == 4:
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif questions[0] == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)