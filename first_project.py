from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"




@app.route('/data/<id>')
def data(id: str):
    return f"fuck_{id}"


if __name__ == "__main__":
    app.run(debug=True,port=3002)
