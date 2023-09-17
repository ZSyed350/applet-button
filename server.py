from flask import Flask, request, jsonify
from flask_cors import CORS
from gpt_loop import code_loop
import subprocess
import os
import fcntl
import time
app = Flask(__name__)
CORS(app)
processes = {}
@app.route('/generate', methods=['POST'])
def code_generation():
    prompt0 = request.form['prompt']
    code, test_cases, error, icon = code_loop(prompt0, is_server=True)
    response = {
        'code': code,
        'test_cases': test_cases,
        'error': error,
        'icon': icon
    }
    return response, 200

@app.route('/feedback', methods=['POST'])
def user_feedback():
    title = request.form['title']
    prompt0 = request.form['prompt']
    feedback = request.form['feedback']
    code, test_cases, error, icon = code_loop(prompt0, title=title, user_feedback=feedback,is_server=True)
    response = {
        'code': code,
        'test_cases': test_cases,
        'error': error,
        'icon': icon
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

@app.route('/get_community_apps', methods=['POST'])
def get_community_apps():
    # get the list of files in the applets folder
    applets = os.listdir('community')
    # remove the .py extension
    applets = [applet[:-3] for applet in applets]
    response =  {
        'applets' : applets
    }
    return response, 200

@app.route('/run-applet', methods=['POST'])
def run_applet():
    data = request.get_json()
    app_name = data.get('app_name')

    result = f"Received: {app_name}"
    # Call applet here
    return jsonify({'result': result})
    
@app.route('/start_script', methods=['POST'])
def start_script():
    script_name = './applets/'+ request.json.get('script_name')  # Get script name from request
    if not script_name:
        return jsonify({"error": "Please provide a script name"}), 400

    # Start the script process
    process = subprocess.Popen(["python3", script_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True)

    # Generate a unique id for the process (For demonstration purpose using process's pid)
    pid = str(process.pid)
    processes[pid] = process
    output = []
    def set_fd_nonblocking(fd):
        """
        Set the file description of the given file to non-blocking.
        """
        flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    # Set stdout of the process to non-blocking mode
    set_fd_nonblocking(process.stdout.fileno())
    time.sleep(1)
    def get_output():
        result = []
        while True:
            try:
                line = process.stdout.readline().strip()
                if not line:
                    break
                print(line)
                result.append(line)
            except IOError:
                break
        return result

    # Get the output before writing user input
    output.extend(get_output())
    return jsonify({"message": "Script started", "pid": pid, "output":output}), 200

@app.route('/interact', methods=['POST'])
def interact():
    output = []
    pid = request.json.get('pid')
    user_input = request.json.get('input')

    if not pid:
        return jsonify({"error": "Please provide a process ID"}), 400

    process = processes.get(pid)
    if not process:
        return jsonify({"error": "Process not found"}), 404

    def set_fd_nonblocking(fd):
        """
        Set the file description of the given file to non-blocking.
        """
        flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

    # Set stdout of the process to non-blocking mode
    set_fd_nonblocking(process.stdout.fileno())

    def get_output():
        result = []
        while True:
            try:
                line = process.stdout.readline().strip()
                if not line:
                    break
                print(line)
                result.append(line)
            except IOError:
                break
        return result

    # Get the output before writing user input
    output.extend(get_output())

    # Write user input and get output again
    print(user_input)
    try:
        process.stdin.write(user_input + '\n')
        process.stdin.flush()
    except:
        return jsonify({"output": output,"functionDone": True}), 200
    time.sleep(0.5)
    # Get the output after writing user input
    output.extend(get_output())

    return jsonify({"output": output}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
