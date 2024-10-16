from flask import Flask

app = Flask(__name__)
print(__name__)


def make_bold(fun):
    def wrapper():
        return '<b>' + fun() + '</b>'
    return wrapper
def make_emphasis(fun):
    def wrapper():
        return '<em>' + fun() + '</em>'
    return wrapper
def make_underlined(fun):
    def wrapper():
        return '<u>' + fun() + '</u>'
    return wrapper

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello():
    return "Hello, World!"

if __name__=='__main__':
    app.run(debug=True)




