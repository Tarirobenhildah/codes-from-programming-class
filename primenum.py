def generate_primes(n):
    for num in range(1, n):
        is_prime = True
        for x in range(2, num):
            if num % x == 0:
                is_prime = False
                break
        if is_prime:
            yield num