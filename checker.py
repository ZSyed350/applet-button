
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    print("Welcome to the calculator!")
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter the operation number: ")
    
    if operation not in ["1", "2", "3", "4"]:
        print("Invalid operation!")
        return
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operation == "1":
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    elif operation == "2":
        result = subtract(num1, num2)
        print(f"The difference between {num1} and {num2} is: {result}")
    elif operation == "3":
        result = multiply(num1, num2)
        print(f"The product of {num1} and {num2} is: {result}")
    elif operation == "4":
        if num2 == 0:
            print("Cannot divide by zero!")
            return
        result = divide(num1, num2)
        print(f"The division of {num1} by {num2} is: {result}")

calculator()
 
# Here is the Python test case code that will validate if the calculator function works correctly.

def test_calculator():
    # Test addition
    assert add(2, 3) == 5
    assert add(-5, 10) == 5
    assert add(0, 0) == 0

    # Test subtraction
    assert subtract(5, 3) == 2
    assert subtract(10, -5) == 15
    assert subtract(0, 0) == 0

    # Test multiplication
    assert multiply(2, 3) == 6
    assert multiply(-5, 10) == -50
    assert multiply(0, 5) == 0

    # Test division
    assert divide(6, 3) == 2
    assert divide(10, -5) == -2
    assert divide(0, 5) == 0

    # Test division by zero
    assert divide(10, 0) == float('inf')

    # Test invalid operation
    assert calculator() == None

# Run the test suite
def main():
    test_calculator()

if __name__ == "__main__":
    main()