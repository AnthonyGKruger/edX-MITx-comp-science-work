primes = []
prime_check = 1

while True:
    prime_check += 1
    for i in primes:
        if prime_check % i == 0:
            break
    else:
        primes.append(prime_check)
        print(prime_check)
