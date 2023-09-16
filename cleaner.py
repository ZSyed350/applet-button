def extract_python_code(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    inside_code_block = False
    python_code = []

    for line in lines:
        stripped_line = line.strip()

        # Check for start of Python code block
        if stripped_line == "```python":
            inside_code_block = True
            continue
        # Check for end of Python code block
        elif stripped_line == "```" and inside_code_block:
            inside_code_block = False
            continue

        # If inside a code block, append the line to python_code list
        if inside_code_block:
            python_code.append(line)

    return ''.join(python_code)

# Example usage:
filename = "./cleaner_test.md"
cleaned_code = extract_python_code(filename)
print(cleaned_code)





