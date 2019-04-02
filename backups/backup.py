from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">

            <label for="rot">Rotate by: </label>
            <input type="text" name="rot" value="0" />

            <textarea name="text">{0}</textarea>

            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot_key = request.form['rot']
    rot_key = int(rot_key)
    user_msg = request.form['text']

    result = rotate_string(rot_key, user_msg)

    ret_form = form.format(result)
    return ret_form

@app.route("/")
def index():
    return form.format("")

app.run()