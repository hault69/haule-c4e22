from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to C4E!!"

@app.route("/quan")
def hello_quan():
    return "hello Quan"

@app.route("/praise/linh")
def praise_linh():
    return "linh is awnsome"

@app.route("/praise/<name>")
def praise(name):
    return name + " is awesome"

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    return str(x + y)

@app.route("/question")
def show_question():
    return render_template("question.html")

if __name__ == "__main__":
    app.run(debug=True)
