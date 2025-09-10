
from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def user():
	return render_template("usercreate.html")
	
@app.route("/regform")
def create():
	return render_template("usercreate.html")
	
@app.route("/logform")	
def log():
	return render_template("lo.html")
	
if __name__ == "__main__":
	app.run(debug=True, port=5007)