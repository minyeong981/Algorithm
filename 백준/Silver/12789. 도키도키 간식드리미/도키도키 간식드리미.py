N = int(input())
numbers = list(map(int, input().split()))
st = []
num = 1

while numbers :
    if numbers[0] == num :
        numbers.pop(0)
        num += 1
    else:
        st.append(numbers.pop(0))

    while st and st[-1] == num :
        st.pop()
        num += 1

print('Nice' if not st else 'Sad')