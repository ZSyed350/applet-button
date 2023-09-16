
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Welcome to the calculator!")
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = add(num1, num2)
        print("The result is:", result)
    elif choice == "2":
        result = subtract(num1, num2)
        print("The result is:", result)
    elif choice == "3":
        result = multiply(num1, num2)
        print("The result is:", result)
    elif choice == "4":
        result = divide(num1, num2)
        print("The result is:", result)
    else:
        print("Invalid choice")

calculator()
