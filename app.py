from flask import Flask, render_template, request
# from flask_socketio import SocketIO
# import SpeechToText

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'
# socketio = SocketIO(app)
ans = []


@app.route('/', methods=["GET"])
def index():
    global ans
    return render_template("editor.html", code=ans, realcode="", script="")


@app.route('/send_data', methods=["POST"])
def index1():
    global ans
    # CODE.append(request.form.get("code", False))
    code = request.form.get("code", False)
    orig = request.form.get("realcode", False)
    script = request.form.get("script", False)
    print(code)
    ans = []
    try:
        val = exec(code)
    except:
        ans = ["THERE HAS BEEN AN ERROR PROCESSING YOUR CODE"]
    print("ANS UNDER")
    print(ans)
    # print(val)
    print(code, orig, script)
    return render_template("editor.html", code=ans, realcode=orig, script=script)


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
    global ans
    ans.append(code)
    return render_template("index.html", code=ans)


if __name__ == '__main__':
    app.run(port=5000)
    # socketio.run(app)
