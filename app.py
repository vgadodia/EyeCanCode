from flask import Flask, render_template, request
from flask_socketio import SocketIO
# import SpeechToText

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'
# socketio = SocketIO(app)
CODE = []


@app.route('/', methods=["GET"])
def index():
    return render_template("editor.html", code=CODE)


@app.route('/', methods=["POST"])
def index1():
    global CODE
    CODE.append(request.form.get("code", False))
    return render_template("index.html", code=CODE)


# @socketio.on('message')
# def handle_message(message):
#     print('received message: ' + message)


@app.route('/editor.html')
def edit():
    return render_template("editor.html")

@app.route('/academy.html')
def aca():
    return render_template("academy.html")

@app.route('/<string:code>', methods=["POST", "GET"])
def display(code):
    global CODE 
    CODE.append(code)
    return render_template("index.html", code=CODE)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    # socketio.run(app)
