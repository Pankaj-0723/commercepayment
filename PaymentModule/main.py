from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def payment_sucess():
    return render_template("index.html")



if os.environ['USERDOMAIN'] == "LAPTOP-GI6I6SB7":
    app.run(debug=True)