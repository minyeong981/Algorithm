s = list(map(int, input()))
# print(len(s)) # 예제3 39
# print(sum(s[2:21])) # 예제3 75
# print(sum(s[21:39])) # 예제3 75

maxV = -1 # 최대 길이
for standI in range(len(s)) : # 기준
    for j in range(standI+1, len(s)) :
        standLength = len(s[standI:j])
        if j+standLength <= len(s) and sum(s[standI:j]) == sum(s[j:j+standLength]) :
            if maxV < standLength :
                maxV = standLength

if maxV == -1 :
    print(0)
else:
    print(maxV*2)