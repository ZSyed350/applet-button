def hello_world():
    return "Hello, world!"

def test_hello_world():
    assert hello_world() == "Hello, world!"

def main():
    test_hello_world()

if __name__ == "__main__":
    main()