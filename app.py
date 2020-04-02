from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/demo")
def demo_page():
    return "Welcome. This is a Demo."

if __name__ == "__main__":
    app.run()
