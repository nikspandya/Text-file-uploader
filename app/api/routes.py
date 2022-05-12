import collections
import os
import random
import uuid
from flask import Response, jsonify, redirect, render_template, request
from flask_accept import accept
from werkzeug.utils import secure_filename
from api import app
from api.helper import get_latest_file, sort_list


abs_path_api = os.path.dirname(os.path.abspath(__file__))
upload_path = os.path.join(abs_path_api, 'uploaded_files')


'''
This route render a html template to provide file upload
'''

@app.route("/", methods=['GET'])
def upload():
    return render_template("upload.html")


'''
This route takes the uploaded file via http post request
and saves it to the folder '/uploaded_files' with secured filename
'''

@app.route("/uploaded", methods=['POST'])
def uploaded_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        # Redirect to upload route again if no file is selected by user
        if uploaded_file.filename == '':
            return redirect("/")
        # If user uploaded text file then store it to uploaded files
        if uploaded_file.filename.lower().endswith(('.txt')):
            # Use unique and secured filename to avoid errors
            uploaded_file_name = str(
                uuid.uuid4()) + '__' + secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(upload_path, uploaded_file_name))
            return jsonify({"message": "file has been uploaded sucessfully"})
        else:
            return render_template("error.html")


'''
Request accept header is mandatory for this route
This route will return the response: one random line of a previously uploaded file via http
as a 'text/plain','application/json' or 'application/xml' depending on the request accept header.
If the request is 'application/*' this route will return json response with one random line,
line number, filename and the letter which occurs most often in the line
'''

@app.route("/one-random-line", methods=['GET'])
@accept('text/plain', 'application/json', 'application/xml', 'application/*')
def get_one_random_line():
    latest_file = get_latest_file(upload_path)
    file_name = latest_file.split('__')[-1]
    file = open(latest_file, "r")
    all_lines = {}
    for idx, line in enumerate(file):
        if not line.isspace():
            all_lines[str(idx + 1)] = line
    file.close()
    try:
        line_number, random_line = random.choice(list(all_lines.items()))
        # Get most common letter and letter_count from selected random line
        most_common_letter = collections.Counter(
            random_line.replace(" ", "")).most_common(1)[0]
    except:
        return jsonify({"message": "Please check previously uploaded file (It may be empty)"})

    # Return response based on request accept header
    accept_header = request.headers['Accept']
    if accept_header == 'text/plain':
        return Response(random_line, content_type='text/plain')

    elif accept_header == 'application/json':
        return Response(random_line, content_type='application/json')

    elif accept_header == 'application/xml':
        return Response(random_line, content_type='application/xml')

    else:
        return jsonify({"random_line": random_line, "line_number": line_number, "file_name": file_name, "most_common_letter": most_common_letter})


'''
This route will render a html template which shows 20 longest lines of the
previously uploaded text file when requested
'''

@app.route("/twenty-longest-lines", methods=['GET'])
def get_twenty_long_lines():
    latest_file = get_latest_file(upload_path)
    with open(latest_file) as l_file:
        lines = (line.rstrip() for line in l_file)
        # Non-blank lines only
        all_lines = list(line for line in lines if line)
    if len(all_lines) < 20:
        return render_template("twenty-lines.html", data=sort_list(all_lines))
    else:
        return render_template("twenty-lines.html", data=sort_list(all_lines)[-20:])


'''
This route will render a html template which shows 100 longest lines of all the
text files when requested
'''

@app.route("/hundred-longest-lines", methods=['GET'])
def get_hundred_longest_lines():
    files = os.listdir(upload_path)
    file_paths = [os.path.join(upload_path, filename) for filename in files]
    all_lines = []
    for txt_file in file_paths:
        file = open(txt_file, "r")
        for line in file:
            if not line.isspace():
                all_lines.append(line)
        file.close()
    if len(all_lines) < 100:
        return render_template("hundred-lines.html", data=sort_list(all_lines))
    else:
        return render_template("hundred-lines.html", data=sort_list(all_lines)[-100:])
