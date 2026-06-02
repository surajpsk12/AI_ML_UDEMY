from flask import Flask, request, render_template

#instance of flask 
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask app"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")



@app.route("/form" ,methods=["GET","POST"])
def form():
    if request.method == "POST":
        # Process form data
        name = request.form.get("name")
        email = request.form.get("email")
        # You can add code here to save the data to a database or perform other actions
        return f"Form submitted successfully! Name: {name}, Email: {email}"
    return render_template("form.html")

@app.route("/about" , methods=["GET"])
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

