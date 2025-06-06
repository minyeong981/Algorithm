def solution(prices):
    answer = []
    n = len(prices)
    for i, price in enumerate(prices) :
        j = i
        while j < n-1 :
            if price > prices[j] :
                break
            j += 1
        answer.append(j-i)
            
    return answer