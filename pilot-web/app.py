from flask import Flask, render_template,request
import mlab
from random import choice
from poll import Poll

app = Flask(__name__)

mlab.connect()

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/poll/<poll_code>")
def poll(poll_code):
  #1. get poll
  
  #objects(yob__gt=1990)

  poll_list = Poll.objects(code=poll_code) #filter data
  # print(poll_list)
  poll = poll_list[0]

  # #2. render
  return render_template("poll.html",p = poll)


@app.route("/polls")
def polls():
  #1 read all polls
  poll_list = Poll.objects()

  #2 render all polls
  return render_template("polls.html", polls = poll_list)

@app.route("/new_poll", methods=["GET","POST"])
def new_poll():
  if request.method == "GET":
    return render_template("new_poll.html")
  elif request.method == "POST":
    #1 unpack data (form)
    form = request.form 
    question = form['question']
    options = []
    for k,v in form.items():
      if k != "question":
        options.append(v)
    print(question)
    print(options)
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789".upper()
    code =" "
    for _ in range(6):
        code += choice(alphabet)
    print(code)
    p = Poll(question = question, options = options, code = code)
    p.save()
    return "Gotcha"


if __name__ == '__main__':
  app.run(debug=True)