#1
class StringProcessor:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print("String in uppercase:", self.string.upper())

processor = StringProcessor()
processor.getString()
processor.printString()


#2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2

shape = Shape()
print("Area of the shape:", shape.area())  # Output: 0

square = Square(5)
print("Area of the square:", square.area())  # Output: 25


#3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 4)
print("Area of the rectangle:", rectangle.area()) 


#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example usage:
point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()

print("Distance between the points:", point1.dist(point2))

point1.move(3, 5)
point1.show()

#5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeds available balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")

# Example usage:
account = BankAccount("John Doe", 1000)
print(f"Account owner: {account.owner}, Initial balance: {account.balance}")

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)



#6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)
