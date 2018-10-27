from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to My Website"

@app.route("/about-me")
def about_me():
    return render_template("profile.html")

@app.route("/school")
def school():
  return redirect("http://techkids.vn")


if __name__ == '__main__':
  app.run(debug=True)