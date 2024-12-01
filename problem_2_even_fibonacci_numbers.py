from utils import is_even

fibonacci_numbers = [0, 1]

while fibonacci_numbers[-1] <= 4 * 10 ** 6:
    fibonacci_numbers.append(fibonacci_numbers[-2] + fibonacci_numbers[-1])

result = 0
for n in fibonacci_numbers:
    if is_even(n):
        result += n

print(result)