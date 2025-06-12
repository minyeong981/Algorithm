def solution(price, money, count):
    total_price = sum([price*i for i in range(1, count+1)])
    return total_price - money if total_price > money else 0