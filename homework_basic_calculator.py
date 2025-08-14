# Homework: Basic Arithmetic Calculator

print("Welcome to the Basic Calculator!")

operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    # TODO: Implement
    result = 0
elif operator == "*":
    # TODO: Implement
    result = 0
elif operator == "/":
    # TODO: Implement with zero check
    result = 0
else:
    print("Invalid operator!")
    result = None

if result is not None:
    print(f"Result: {result}")

