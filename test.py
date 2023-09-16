# Here is the Python test case
def test_hello_world():
    assert hello_world() == "Hello, world!"

# Write a main function that will run the test suite when run as the file
def main():
    test_hello_world()

# Run the main function
if __name__ == "__main__":
    main()