from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
    #1 unpack data (form)
        form = request.form 
        firstname = form['fist_name']
        lastname = form['last_name']
        mail = form['email']
        yob = form['yob']
        gender = form['gender']
        city = form['city']
        print(firstname+" "+lastname,mail,yob,gender,city, sep=" , ")
        return "Successful"


if __name__ == '__main__':
  app.run(debug=True)