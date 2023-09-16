import os
import openai 
import subprocess 
import dotenv

from helpers.openai import Model
from pathlib import Path

ENGINE = Model.GPT_3_5_TURBO
MAX_TOKENS = 2048
FEEDBACK = ""

# LOAD API KEY FROM ENV FILE
dotenv.load_dotenv()
assert os.getenv("API_KEY") is not None, "Set API_KEY in .env file"
openai.api_key = os.getenv("API_KEY")

def get_chat_response(prompt: str) -> str:
    """Get a chat response using the language model API"""
    global FEEDBACK
    if FEEDBACK != "":
        prompt = f"This is what should be most important. Modify the code to follow the feedback as given: {feedback} \n{prompt}"
        response = openai.ChatCompletion.create(
            model=ENGINE,
            messages=[{"role": "user",
                       "content": prompt}],
            temperature=0.5,
            max_tokens=MAX_TOKENS,
        )
        completion = response["choices"][0]["message"]["content"]
    filtered_completion = completion.replace(
        "```python", "").replace("```", "")
    return filtered_completion

def gen_code_from_prompt(prompt: str) -> str:
    print("Generating code")
    prompt = f"Only return python code to this problem with proper indentation and do not include any test suite in the output if given: {prompt}\nPython script:"
    return get_chat_response(prompt)

def gen_test_cases_from_prompt(prompt: str) -> str:
    print("Generating test cases")
    prompt = f"{prompt}\nOnly write the Python test case code that will validate if the function works and write a main function that will run the test suite when run as the file and if the python function uses a gui then do not write proper tests and write one test that will return true after running the function:"
    return get_chat_response(prompt)

def gen_file_name_from_prompt(prompt: str) -> str:
    print("Generating file name")
    prompt = f"Create a short python file name with the file extension for this task: {prompt}"
    return get_chat_response(prompt)

def write_code_to_file(code: str, filename: str):
    print("Writing code to file")
    with open(filename, 'w') as f:
        f.write(code)

def run_code(filename: str) -> str:
    print("Running code")
    """Run a Python code file and return the error output."""
    process = subprocess.Popen(
        ['python3', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stderr = process.communicate()
    return stderr.decode()

save_dir = Path(__file__).parent / "generated"

print(save_dir)
