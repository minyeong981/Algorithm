string = input()
baam = list(input())
N = len(string)
M = len(baam)

st = []
for i in string :
    st.append(i)
    if len(st) >= M :
        if st[-M:] == baam :
            for _ in range(M) :
                st.pop()
if st :
    print(''.join(map(str,st)))
else :
    print('FRULA')