import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {executor.submit(is_prime, prime): prime for prime in PRIMES}

        for future in concurrent.futures.as_completed(results):
            prime = results[future]
            try:
                is_prime_result = future.result()
            except Exception as exc:
                print(f"{prime} generated an exception: {exc}")
            else:
                print(f"{prime} is prime: {is_prime_result}")

if __name__ == "__main__":
    main()
