def hello_world():
    return "Hello, World!" 
# Here is the Python test case
def test_hello_world():
    assert hello_world() == "Hello, World!"

# Run the test suite
def main():
    test_hello_world()

if __name__ == "__main__":
    main()