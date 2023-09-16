print("Hello") 
# Here is the Python test case
def test_hello():
    assert print("Hello") == None

def main():
    test_hello()

if __name__ == "__main__":
    main()