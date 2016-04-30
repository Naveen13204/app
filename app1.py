import os
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def homepage():
    return render_template("app2.html")
@app.route('/dashboard/')
def dashboard():
    return render_template("app2.html")

if __name__=='__main__':
      app.debug=True
      port=int(os.environ.get('PORT',5000))	
      app.run(host='127.0.0.1',port=5000)
