# The Python function count_digit_occurrences counts the occurrences of each digit in a given list. Here’s how it works:
#
# The function initializes an empty dictionary called digit_counts.
# It iterates through each digit in the input list.
# If the digit is between 0 and 9, it updates the count for that digit in the dictionary.
# The function returns the dictionary containing the occurrences of each digit.

def count_digit_occurrences(digits_list):

    digit_counts = {}  # Initialize an empty dictionary

    for digit in digits_list:
        if 0 <= digit <= 9:

            digit_counts[digit] = digit_counts.get(digit, 0) + 1

    return digit_counts

# Example usage:
user_input = input("Enter a list of digits (0-9), separated by spaces: ")
try:
    input_list = [int(digit) for digit in user_input.split()]
    result = count_digit_occurrences(input_list)
    print("Digit occurrences:", result)
except ValueError:
    print("Invalid input. Please enter valid digits (0-9).")