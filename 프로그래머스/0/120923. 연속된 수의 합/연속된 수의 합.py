def solution(num, total):
    base = total // 2
    window = [value for value in range(base-num, base)]
    if sum(window) != total :
        error = abs(sum(window) - total)
        for _ in range(error) :
            if sum(window) > total :
                window = [window[0]-1] + window[:num-1]   
            elif sum(window) < total :
                window = window[1:] + [window[-1]+1] 
            else :
                break
    return window