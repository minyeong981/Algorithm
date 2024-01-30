N, M = map(int, input().split())

lst = []
for idx in range(N) :
    lst.append(idx+1)
for _ in range(M) : #m=4면
    i, j = list(map(int, input().split())) #4번 반복
    lst[i-1:j] = reversed(lst[i-1:j]) # i ~ j까지 범위 정하기 > 역순으로 바꾸기
print(*lst)