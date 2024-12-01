from utils import is_palindromic

list_of_palindromic_numbers = []

i = 100
while i < 1000:
    j = 100
    while j <= i:
        result = i * j
        if is_palindromic(result):
            list_of_palindromic_numbers.append(result)
        j += 1
    i += 1

result = max(list_of_palindromic_numbers)
print(result)
