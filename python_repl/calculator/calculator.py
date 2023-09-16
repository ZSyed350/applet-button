
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
fifo_path = "/tmp/my_pipe"
def calculator():
    print("Welcome to the calculator!")
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    with open(fifo_path, "r") as fifo:
        data = fifo.readline().strip() 
        operation = fifo.readline().strip()  
        
        if operation not in ["1", "2", "3", "4"]:
            print("Invalid operation!")
            return
        
        num1 = float(fifo.readline().strip()  )
        num2 = float(fifo.readline().strip()  )
    
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
