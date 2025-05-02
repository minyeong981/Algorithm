def solution(citations):
    n = len(citations)
    citations.sort()
    answer = 0
    for h in range(1, n+1) :
        cnt = 0
        for j in range(n) :
            if h <= citations[j] :
                cnt += 1
        if h <= cnt and h >= n - cnt :
            answer = max(answer, h)

    return answer