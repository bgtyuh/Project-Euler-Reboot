from utils import SmoothSort, remove_duplicates

multiples_of_three = [3 * i for i in range(1, 334)]
multiples_of_five = [5 * i for i in range(1, 200)]

multiples_of_three_or_five = multiples_of_three + multiples_of_five

sorter = SmoothSort()
multiples_of_three_or_five = sorter.smooth_sort(multiples_of_three_or_five)

multiples_of_three_or_five = remove_duplicates(multiples_of_three_or_five)

result = sum(multiples_of_three_or_five)

print(result)