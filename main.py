from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="post">

            <label for="rot">Rotate by: </label>
            <input type="text" name="rot" value="0" />

            <input type="textarea" name="text" />

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
    #return "rot amount = " + rot_key + ", user message = " + user_msg

    result = rotate_string(rot_key, user_msg)

    return '<h1>' + result + '</h1>'

@app.route("/")
def index():
    return form

app.run()