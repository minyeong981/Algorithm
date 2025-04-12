def funcMul(a, b) :
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]
    ]

def funcPow(matrix, n) :
    result = [[1, 0], [0, 1]] # 단위 행렬 : 곱셈에서 아무 영향 없는 기본값
    while n :
        if n % 2 :
            result = funcMul(result, matrix)
        matrix = funcMul(matrix, matrix)
        n //= 2
    return result

def fib(n) :
    if n == 0 :
        return 0
    base = [[1, 1], [1, 0]] # 피보나치 계산용 기본 행렬
    res = funcPow(base, n - 1) # base를 n-1 제곱하기
    return res[0][0] # F(n)의 값

mod = 10**9 + 7
n = int(input())
print(fib(n))