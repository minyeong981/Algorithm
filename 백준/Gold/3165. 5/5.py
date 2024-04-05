N, K = map(int, input().split())

#냅다 1씩 더해주기
N += 1
numlst = list(str(N))
i = -1 # 맨 뒷자리부터 바꿔줘야 하니까
maxi = len(numlst) # 인덱스 에러 안 나게

while True :
    if numlst.count('5') >= K : # 5의 개수가 K개 이상이면
        break

    while numlst[i] == '5' and abs(i) < maxi : # 해당 인덱스 부분이 5이고, 가장 클 수 있는 인덱스 크기보다 작을 경우
        i -= 1  # 인덱스 역순으로 늘려주기(-1 -> -2)

    result = int(''.join(numlst))
    result = result + 10**(abs(i)-1)
    numlst = list(str(result))
    maxi = len(numlst)

print(''.join(numlst))

