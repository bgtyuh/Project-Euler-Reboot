from utils import divisors_of, is_prime

list_of_divisors = divisors_of(600_851_475_143, fast_for_prime_factors=True)

prime_factors = []
for n in list_of_divisors:
    if is_prime(n):
        prime_factors.append(n)

result = max(prime_factors)
print(result)