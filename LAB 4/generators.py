#1
def squares_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

N = int(input("Enter a number:"))
squares = squares_generator(N)

print(f"Squares of numbers up to {N}:")
for square in squares:
    print(square)


#2
def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter the value of n: "))
even_numbers = even_numbers_generator(n)

print("Even numbers between 0 and", n, ":", end=" ")
for num in even_numbers:
    print(num, end=", ")
print() 


#3
def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    n = int(input("Enter the value of n: "))
    print("Numbers between 0 and", n, "divisible by both 3 and 4:")
    for num in divisible_by_3_and_4_generator(n):
        print(num, end=", ")

if __name__ == "__main__":
    main()


#4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

# Test the generator with a for loop2
a = 3
b = 7

print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)


#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input("Enter a number for a Countdown:"))

print(f"Countdown from {n} to 0:")
for num in countdown(n):
    print(num)
