from flask import Flask, render_template, request
# from flask_socketio import SocketIO
# import SpeechToText

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'
# socketio = SocketIO(app)
ans = []
code = ""
orig = ""
script = ""

@app.route('/', methods=["GET"])
def index():
    global ans
    return render_template("index.html", code=ans, realcode="", script="")


@app.route('/send_data', methods=["GET", "POST"])
def index1():
    global code, orig, script
    # CODE.append(request.form.get("code", False))
    code1 = request.form.get("code", False)
    orig1 = request.form.get("realcode", False)
    script1 = request.form.get("script", False)
    if code1 and orig1 and script1:
        code = code1
        orig = orig1
        script = script1
    print(code)
    ans = []
    # code = "ans.append('hello world')"
    # orig = "print(\"hello world\")"
    # script = "print string hello world"
    try:
        val = exec(code)
    except:
        ans = ["THERE HAS BEEN AN ERROR PROCESSING YOUR CODE"]
    print("ANS UNDER")
    print(ans)

    # print(val)
    print(code)
    print(orig)
    print(script)
    return render_template("editor.html", code=ans, realcode=orig.split("\n"), script=script)


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
    app.run(port=5000, debug=True)
    # socketio.run(app)
