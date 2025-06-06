def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i, price in enumerate(prices) :
        while stack != [] and stack[-1][1] > price :
            j, _ = stack.pop()
            answer[j] = i - j
        stack.append([i, price])

    for i, price in stack :
        answer[i] = n - i - 1
            
    return answer