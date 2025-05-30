1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
def to_int(string):
    l = len(string)
    a = 0
    for i in range(l):
        a += (ord(string[l - 1 - i]) - 96) * pow(26,i)
    return a
def to_string(i):
    s = ''
    while i > 0:
        i -= 1 
        s = chr(i % 26 + 97) + s
        i //= 26
    return s

def solution(n, bans):
    bans_sort = sorted(bans, key = lambda x: (len(x), x))

    for b in bans_sort:
        if to_int(b) <= n:
            n += 1
        else:
            break
    return to_string(n)