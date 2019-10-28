import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    birthday = now.month == 4 and now.day == 25
    names = ["Levinson", "Bakugo", "Izuku"]
    return render_template("index.html", birthday=birthday, names=names)

if __name__ == "__main__":
    app.run(debug=True)