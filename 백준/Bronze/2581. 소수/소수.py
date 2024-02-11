M = int(input())
N = int(input())
sum_primes = 0
min_prime = None

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(M, N+1):
    if is_prime(num):
        sum_primes += num
        if min_prime is None or num < min_prime:
            min_prime = num

if min_prime is not None:
    print(sum_primes)
    print(min_prime)
else:
    print(-1)