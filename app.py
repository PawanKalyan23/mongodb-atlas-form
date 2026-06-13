from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection String
MONGO_URI = "mongodb+srv://pawan23_db_user:Pawan23@cluster0.rt3cfr7.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

# Database and Collection
db = client["studentdb"]
collection = db["students"]


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        email = request.form["email"]

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect("/success")

    except Exception as e:
        return render_template(
            "form.html",
            error=str(e)
        )


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
