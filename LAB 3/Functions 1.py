#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

def main():
    grams = int(input())
    ounces = grams_to_ounces(grams)
    print(ounces)

if __name__ == "__main__":
    main()


#2
def fahrenheit_to_ceclium(F):
    C = (5 / 9) * (F - 32)
    return C

def main():
    F = int(input())
    C = fahrenheit_to_ceclium(F)
    print(C)

if __name__ == "__main__":
    main()


#3
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits
        if total_legs == numlegs:
            return num_chickens, num_rabbits
    return "No solution"

def main():
    numheads = 35
    numlegs = 94
    solution = solve(numheads, numlegs)
    if solution != "No solution":
        num_chickens, num_rabbits = solution
        print(f"Number of chickens: {num_chickens}")
        print(f"Number of rabbits: {num_rabbits}")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()


#4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)


#5
from itertools import permutations

def print_permutations(input_string):
    perm_list = permutations(input_string)
    for perm in perm_list:
        print(''.join(perm))

def main():
    input_string = input()
    print_permutations(input_string)

if __name__ == "__main__":
    main()


#6
def reverse_sentence(input_string):
    words = input_string.split()
    reversed_words = reversed(words)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

def main():
    input_string = input()
    reversed_sentence = reverse_sentence(input_string)
    print(reversed_sentence)

if __name__ == "__main__":
    main()


#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i:i+2] == [3, 3]:
            return True
    return False

print(has_33([1, 3, 3]))   
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))    


#8
def spy_game(nums):
    code = [0, 0, 7]  
    index = 0  
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0])) 


#9
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = 5
volume = sphere_volume(radius)
print("Volume of the sphere with radius", radius, "is:", volume)


#10
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

original_list = [1, 2, 3, 3, 4, 5, 5, 5]
unique_list = unique_elements(original_list)
print("Original list:", original_list)
print("Unique elements list:", unique_list)


#11
def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]


word = "A man, a plan, a canal, Panama!"
print(f'"{word}" is a palindrome:', is_palindrome(word))


#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
numbers = [4, 9, 7]
histogram(numbers)


#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()

