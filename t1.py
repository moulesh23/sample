from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ques", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["num"]
        user=int(user)
        ans=5
        if(user==ans):
            return f"Correct Answer "
        else:
            return f"Wrong Answer "
    else:
        return render_template("ques.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
