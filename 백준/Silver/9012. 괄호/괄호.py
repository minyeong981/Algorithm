T = int(input())
for tc in range(1, T+1) :
    ps = input()
    result = True #변수 초기화!!!
    lst = []
    for c in ps :
        if c == '(' :
            lst.append(c)
        elif c == ')':
            if len(lst) > 0 and lst.pop() == '(' :
                continue
            else :
                result = False
    if len(lst) > 0 :
        result = False
    if result :
        print('YES')
    else :
        print('NO')