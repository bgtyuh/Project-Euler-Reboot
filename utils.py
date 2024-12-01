import numpy as np


class SmoothSort:
    def __init__(self):
        pass  # No need for initialization since no persistent state is required

    def restore_heap(self, arr, root, n):
        """
        Restore the heap property for a subtree rooted at the given index.
        Ensures the parent is greater than its children.
        """
        largest = root  # Assume the root is the largest
        left = 2 * root + 1  # Index of the left child
        right = 2 * root + 2  # Index of the right child

        # Check if the left child exists and is greater than the root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if the right child exists and is greater than the largest found so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the root is not the largest, swap it with the largest and restore the heap
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            # Recursively restore the heap for the affected subtree
            self.restore_heap(arr, largest, n)

    def build_heap(self, arr):
        """
        Convert the array into a binary heap.
        Start from the last non-leaf node and move up to the root.
        """
        n = len(arr)
        # Loop from the last non-leaf node to the root
        for i in range(n // 2 - 1, -1, -1):
            self.restore_heap(arr, i, n)

    def smooth_sort(self, arr):
        """
        Perform the Smoothsort algorithm to sort the array.
        """
        # Step 1: Build the heap
        self.build_heap(arr)

        # Step 2: Sort the array
        n = len(arr)
        for i in range(n - 1, 0, -1):
            # Move the largest element (root) to the end of the array
            arr[i], arr[0] = arr[0], arr[i]
            # Restore the heap property for the remaining elements
            self.restore_heap(arr, 0, i)

        return arr  # Return the sorted array

def remove_duplicates(array):
    """
    Remove duplicates from a list while maintaining order.
    """
    seen = set()
    return [x for x in array if not (x in seen or seen.add(x))]

def is_even(n):
    """
    Return True if 'n' is event and False otherwise
    """
    return n % 2 == 0

def is_prime(n):
    """
    Return True if 'n' is a prime number and False otherwise
    """
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def divisors_of(n, fast_for_prime_factors = False):
    """
    Return the divisors of 'n' as a list
    """
    list_of_divisors = []
    if fast_for_prime_factors:
        stop = int(np.sqrt(n) + 1)
    else:
        stop = n // 2 + 1
    for i in range(1, stop):
        if n % i == 0:
            list_of_divisors.append(i)
    return list_of_divisors

def is_palindromic(n):
    """
    Return True if 'n' is palindromic
    """
    n_as_string = str(n)
    for i in range(len(n_as_string) // 2):
        if n_as_string[i] != n_as_string[-i - 1]:
            return False
    return True

def is_divisible_from_1_to_20(n):
    """
    Return True if 'n' is divisble by 1, 2, 3, ..., 20 and False otherwise
    """
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

def permutation_replacements(n, replacement):
    """
    Give all the permutations on a given 'n' number of 2 digits replaced by 'replacement'
    """
    list_of_replacements = []
    n_as_string = str(n)
    for i in range(len(n_as_string)):
        for j in range(i + 1, len(n_as_string)):
            permutation = n_as_string[:i] + str(replacement) + n_as_string[i + 1:j] + str(replacement) + n_as_string[j + 1:]
            list_of_replacements.append(int(permutation))
    return list_of_replacements

def number_of_prime_numbers(list_of_numbers):
    """
    Return the number of prime numbers in list_of_numbers
    """
    c = 0
    for n in list_of_numbers:
        if is_prime(n):
            c += 1
    return c

# Test
if __name__ == "__main__":
    sorter = SmoothSort()
    my_array = [5, 3, 8, 1, 2, 7, 4, 6]
    my_sorted_array = sorter.smooth_sort(my_array)
    print("Sorted array:", my_sorted_array)

    my_array = [5, 3, 8, 1, 3, 7, 4, 6, 1]
    print("Original array:", my_array)
    unique_array = remove_duplicates(my_array)
    print("Array without duplicates:", unique_array)

    print("Liste des 10 premiers nombres pairs :", [i for i in range(19) if is_even(i)])

    print("Liste des 10 premiers nombres premiers :", [i for i in range(30) if is_prime(i)])

    print("Les diviseurs de 36 sont :", divisors_of(36))

    print("Le nombre 90109 est un nombre palindrome :", is_palindromic(90109))
    print("Le nombre 59 est un nombre palindrome :", is_palindromic(59))
