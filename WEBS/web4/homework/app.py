from flask import Flask, render_template,request
import mlab
from river import River
app = Flask(__name__)

mlab.connect()

@app.route("/river/<river_continent>")
def river_continent(river_continent):
  #1. get data

  river_list = River.objects(continent=river_continent) #filter data

  # #2. render
  return render_template("river_continent.html",rc = river_list)

@app.route("/river/1000")
def river_length():

  river_list = River.objects(continent = 'S. America', length__lt = 1000)

  return render_template("river_length.html",rl = river_list)

if __name__ == '__main__':
  app.run(debug=True)