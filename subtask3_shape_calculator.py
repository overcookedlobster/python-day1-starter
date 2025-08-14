# Sub-Task 3: Shape Area Calculator
# Combine variables, operations, and I/O.

print("Welcome to the Shape Area Calculator!")

shape = input("Enter the shape (circle, rectangle, triangle): ").lower()

if shape == "circle":
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius ** 2
    print(f"The area is: {area}")
elif shape == "rectangle":
    # TODO: Add inputs and calculation
    print("The area is: ??")
elif shape == "triangle":
    # TODO: Add inputs and calculation
    print("The area is: ??")
else:
    print("Invalid shape!")

