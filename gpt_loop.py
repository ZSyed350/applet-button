import os
import openai
import subprocess
from pathlib import Path

import dotenv
dotenv.load_dotenv()

assert os.getenv(
    "OPENAI_API_KEY") is not None, "Please set OPENAI_API_KEY in .env file"

# Please replace `your-openai-api-key` with your own OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
engine = "gpt-3.5-turbo"
max_tokens = 2048
feedback = ""


def create_openai_chat_response(prompt: str) -> str:
    """Create a chat response using OpenAI API."""
    global feedback
    if feedback != "":
        prompt = f"This is what should be most important. Modify the code to follow the feedback as given: {feedback} \n{prompt}"
    response = openai.ChatCompletion.create(
        model=engine,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=max_tokens,
    )
    completion = response["choices"][0]["message"]["content"]  # type: ignore
    filtered_completion = completion.replace(
        "```python", "").replace("```", "")
    return filtered_completion


def generate_code_from_prompt(prompt: str, error: str = "") -> str:
    print("Generating code")
    """Generate Python code using OpenAI API based on the given prompt."""
    prompt = f"Only return python code to this problem with proper indentation and do not include any test suite in the output if given: {prompt}\nPython script:"
    if error:
        prompt = f"{prompt}\nError encountered, please write code to fix: {error}"

    return create_openai_chat_response(prompt)


def generate_test_cases_from_prompt(prompt: str) -> str:
    print("Generating test cases")
    """Generate Python test cases using OpenAI API based on the given prompt."""
    prompt = f"{prompt}\nOnly write the Python test case code that will validate if the function works. If you provide explanations or extra statements such as 'Here is the Python test case', provide it as a comment with #. Write a main function that will run the test suite when run as the file. If the python function uses a GUI then do not write proper tests and write one test that will return true after running the function:"
    return create_openai_chat_response(prompt)

def generate_code_and_test(prompt0: str):
    print("Generating code and test cases")
    """Generate code and test cases based on the given prompt."""
    code = generate_code_from_prompt(prompt0)
    test_prompt = f"The prompt: {prompt0} \nThe code: {code}"
    test_cases = generate_test_cases_from_prompt(test_prompt)
    return code, test_cases


def generate_file_name_from_prompt(prompt: str) -> str:
    print("Generating filename")
    """Generate file using OpenAI API based on the given prompt."""
    prompt = f"Create a short python file name with the file extension for this task: {prompt}"
    return create_openai_chat_response(prompt)


def write_code_to_file(code: str, filename: str):
    print("Writing code to file")
    """Write the given code to a file with the given filename."""
    with open(filename, 'w') as f:
        f.write(code)


def run_code(filename: str) -> str:
    print("Running code")
    """Run a Python code file and return the error output."""
    process = subprocess.Popen(
        ['python3', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stderr = process.communicate()
    return stderr.decode()

def get_user_feedback():
    """Get user feedback on the generated code."""
    user_input = input("Are you happy with this applet? (y/n): ")
    if user_input.lower() == "y":
        print("Great! Your applet has been saved.")
        return None
    elif user_input.lower() == "n":
        feedback = input("Please entery any feedback.\nFeedback: ")
        return "Human feedback given"
    else:
        return get_user_feedback()
    
def save_and_run_tests(code: str, test_cases: str, title: str):
    """Save the generated code and test cases to files and run the tests."""
    write_code_to_file(code, os.path.join(save_dir, title))
    write_code_to_file(test_cases, 'test.py')
    test_str = f"{code} \n{test_cases}"
    write_code_to_file(test_str, 'checker.py')
    error = run_code("checker.py")
    return error, test_str

def display_code_info(code: str, test_cases: str, error: str):
    """Display the generated code, test cases, and error (if any) to the user."""
    print('=====================')
    print(f"Code: \n{code}")
    print('---------------------')
    print(f"Test Cases: \n{test_cases}")
    print('---------------------')
    print(f"Error: \n{error}")
    print('=====================')


save_dir = Path(__file__).parent / "applets"

print(save_dir)

#TODO co.generate to sprinkle joy
def code_loop(og_prompt: str = "", test_cases: str = "", error: str = "", loop: int = 0, title: str = "", max_loops: int = 10):
    """Run a loop that generates Python code, writes them to files, and runs the code."""

    if loop >= max_loops:
        print("Error: Maximum loop count reached! Process terminated.")
        return
    
    loop += 1
    print(f"Loop: {loop}")

    if not og_prompt:
        og_prompt = input("Please enter the prompt for the task: ")
        title = generate_file_name_from_prompt(
            f"Create a short python file name with the file extension for this task: {og_prompt}")
        code = generate_code_from_prompt(og_prompt)
        if not test_cases:
            test_prompt = f"The prompt: {og_prompt} \nThe code: {code}"
            test_cases = generate_test_cases_from_prompt(test_prompt)

    else:
        code = generate_code_from_prompt(og_prompt, error)

    error, test_str = save_and_run_tests(code, test_cases, title)
    display_code_info(code, test_cases, error)

    if test_str and not error:
        error = get_user_feedback()

    if error:
        code_loop(og_prompt, test_cases, error, loop, title)



if __name__ == "__main__":
    code_loop()