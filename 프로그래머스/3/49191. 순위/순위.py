def solution(n, results):
    relations = [[False] * (n+1) for _ in range(n+1)]
    
    for win, lose in results :
        relations[win][lose] = True
    
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                if relations[i][k] and relations[k][j] :
                    relations[i][j] = True
    answer = 0
    for i in range(1, n+1) :
        winCount = sum(relations[i])
        loseCount = sum([relations[j][i] for j in range(1, n+1)])
        if winCount + loseCount == n - 1 :
            answer += 1
    
    return answer