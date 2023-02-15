from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # return "<h1>Hello Puppy!</h1>"
    return render_template('basic.html')


@app.route("/information")
def info():
    return "<h1>Puppies are cute!</h1>"


@app.route("/puppy/<name>")
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)
    # return "Upper case: {}".format(name.upper())
    # return "100th letter: {}".format(name[100])


@app.route("/puppy_latin/<name>")
def puppyLatin(name):
    latin_name = ''
    if name[-1] == 'y':
        latin_name = name[:-1] + 'iful'
    else:
        latin_name = name + 'y'

    return "Hi {}! Your puppy latin name is {}".format(name, latin_name)


if __name__ == "__main__":
    app.run(debug=True)
