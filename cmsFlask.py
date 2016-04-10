from flask import Flask
from flask import render_template, flash, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/render')
def hello_world():
    return render_template()


if __name__ == '__main__':
    app.run()
