from utils import permutation_replacements, number_of_prime_numbers, is_prime

n = 1
replacement = 0
while number_of_prime_numbers(permutation_replacements(n, replacement)) != 8:
    if replacement < 9:
        replacement += 1
    else:
        replacement = 0
        n += 1

result = n
print(result, replacement)

print(permutation_replacements(result, replacement))

print([i for i in permutation_replacements(result, replacement) if is_prime(i)])