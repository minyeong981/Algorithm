import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
st = [] #인덱스 저장용
result = [-1]*n #오큰수 없으면 -1이니까 -1로 채워두기
st.append(0) #0번째 인덱스 넣어놓고 시작

for i in range(1, n) :
    value = A[i]
    while st :
        if A[st[-1]] < value : #오른쪽 값 비교해서 크면
            result[st.pop()] = value #result에 값 할당
        else :
            break
    st.append(i)
print(*result)