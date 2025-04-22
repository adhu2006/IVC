def top_three_even_numbers(numbers):
    """
    Returns the top 3 even numbers from the given list in descending order.
    If there are fewer than 3 even numbers, returns all of them in descending order.
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_numbers.sort(reverse=True)
    return even_numbers[:3]

# Test cases
test_case_1 = [10, 15, 22, 8, 3, 14, 6]
test_case_2 = [1, 3, 5, 7, 9, 2]

print(top_three_even_numbers(test_case_1))  # Output: [22, 14, 10]
print(top_three_even_numbers(test_case_2))  # Output: [2]