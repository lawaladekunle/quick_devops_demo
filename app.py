from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "Galaxy")
    return f'Hello, {escape(name)}!'

# a simple page that says hello
#    @app.route('/hello')
#    def hello():
#        return 'Hello, World!'

    return app
