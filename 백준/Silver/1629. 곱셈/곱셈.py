def doubleX(a, b, c):
    result = 1
    a = a % c  # 미리 모듈러 연산을 적용

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b //= 2

    return result

a, b, c = map(int, input().split())
print(doubleX(a, b, c))
