def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Improved solution handling potential TypeError
def calculate_average_improved(numbers):
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List elements must be numbers")
    total = sum(numbers)
    average = total / len(numbers)
    return average