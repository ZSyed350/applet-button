from flask import Flask, request
from flask_cors import CORS
from gpt_loop import code_loop
import os
app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def code_generation():
    prompt0 = request.form['prompt']
    code, test_cases, error = code_loop(prompt0, is_server=True)
    response = {
        'code': code,
        'test_cases': test_cases,
        'error': error
    }
    return response, 200

@app.route('/feedback', methods=['POST'])
def user_feedback():
    title = request.form['title']
    prompt0 = request.form['prompt']
    feedback = request.form['feedback']
    code, test_cases, error = code_loop(prompt0, title=title, user_feedback=feedback,is_server=True)
    response = {
        'code': code,
        'test_cases': test_cases,
        'error': error
    }
    return response, 200

@app.route('/get_my_apps', methods=['POST'])
def get_my_apps():
    # get the list of files in the applets folder
    applets = os.listdir('applets')
    # remove the .py extension
    applets = [applet[:-3] for applet in applets]
    response =  {
        'applets' : applets
    }
    return response, 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
