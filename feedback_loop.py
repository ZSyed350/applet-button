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
