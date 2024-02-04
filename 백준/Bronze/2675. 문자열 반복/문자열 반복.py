T = int(input())
for tc in range(T) :
    R, S = input().split()

    lst = []
    for s in S :
        lst.append(s*int(R))
        result = ''.join(lst)
    print(result)