from flask import Flask, render_template
# import SpeechToText

app = Flask(__name__)
CODE = []

@app.route('/')
def index():
    return render_template("index.html", code=CODE)

@app.route('/displayText/<string:code>', methods=["POST", "GET"])
def display(code):
    global CODE 
    CODE.append(code)
    return render_template("index.html", code=CODE)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
