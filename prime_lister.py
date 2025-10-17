
def get_primes(end_num):
    primes = []
    for i in range(end_num + 1):
        is_prime = True
        if i < 2:
            is_prime = False
        for j in range(2, int(i ** .5) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)

    return primes


print(get_primes(100))
