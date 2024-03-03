#1
from functools import reduce

def multiply_list(numbers):
    if not numbers:
        return None
    return reduce(lambda x, y: x * y, numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Result:", result)


#2
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = input("Enter a string: ")
upper, lower = count_upper_lower(input_string)

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)


#3
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4
import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = math.sqrt(number)
    return result

number = 25100
milliseconds = 2123

result = calculate_square_root(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {result}.")


#5
def all_true(elements):
    return all(elements)

tuple_1 = (True, True, True)
tuple_2 = (True, False, True)

print(all_true(tuple_1))
print(all_true(tuple_2)) 

