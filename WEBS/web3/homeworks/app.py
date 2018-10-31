from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("s1.html")
    elif request.method == "POST":
    #1 unpack data (form)
        form = request.form 
        model = form['model']
        fee = form['fee']
        image = form['image']
        year = form['year']
        print(model,fee,image,year, sep=" , ")
        return "Successful"

if __name__ == '__main__':
  app.run(debug=True)