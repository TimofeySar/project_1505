from flask import Flask, render_template
from flask.helpers import url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("jor2.html")


if __name__ == "__main__":
    app.run(debug=True)