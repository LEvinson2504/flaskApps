from flask import Flask
#create new flask web app using current program
app = Flask(__name__)

@app.route("/") #function immediately next will run
def index():
    return "Hello beautiful people!" 

@app.route("/levi")
def levi():
    return "Hello levinson!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello , {name}</h1>"

if __name__ == "__main__":
    app.run(debug=True)