from utils import is_divisible_from_1_to_20

n = 20
while not is_divisible_from_1_to_20(n):
    n += 20

result = n
print(result)