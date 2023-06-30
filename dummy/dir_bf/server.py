from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/webadmin")
def example_secret_dir():
    return "<p>you found the secret directory!</p>"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
