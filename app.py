from flask import Flask, render_template
from flask import flash

app=Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True, port=3000)