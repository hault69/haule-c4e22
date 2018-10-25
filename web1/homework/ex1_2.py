from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
  return "Welcome to My Website"

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
  BMI = weight / ((height/100)*(height/100))
  if BMI < 16:
      return render_template("severlyunderweight.html")
  elif 16 < BMI < 18.5 :
      return render_template("underweight.html")
  elif 18.5 < BMI < 25 :
      return render_template("normal.html")
  elif 25 < BMI < 30 :
      return  render_template("overweight.html")
  else:
      return  render_template("obese.html")

        
 

if __name__ == '__main__':
  app.run(debug=True)