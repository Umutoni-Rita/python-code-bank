# This is a Python program that performs basic Arithmetic Operations

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Division by 0 is not possible")
    return num1 / num2

print(add(18, 34))
print(subtract(18, 34))
print(multiply(18, 34))
print(divide(18, 34))

