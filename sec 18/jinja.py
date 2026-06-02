from flask import Flask, request, render_template, redirect, url_for

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

'''
jinja 2 template engine 
{{ variable }} for variable substitution
{% for item in list %} for loops
{% if condition %} for conditionals
# You can also use filters to modify the output, such as {{ variable|filter }}
'''

# Variable rule example
@app.route("/success/<float:score>")
def success(score):
    res=""
    if score >= 90:
        res = "Excellent"
    elif score >= 80:
        res = "Good"
    elif score >= 70:
        res = "Average"
    else:
        res = "Needs Improvement"

    return render_template("result.html", result=res)

@app.route("/successloop/<float:score>")
def successres(score):
    res=""
    if score >= 90:
        res = "Excellent"
    elif score >= 80:
        res = "Good"
    elif score >= 70:
        res = "Average"
    else:
        res = "Needs Improvement"

    exp = {"result": res, "score": score}

    return render_template("resultloop.html", result=exp) 

@app.route("/submit", methods=["GET", "POST"])
def submit():
    total_score = 0
    if request.method == "POST":
        def safe_int(val, default=0):
            try:
                return int(val)
            except (TypeError, ValueError):
                return default

        science = safe_int(request.form.get("science"))
        math = safe_int(request.form.get("math"))
        english = safe_int(request.form.get("english"))
        data_science = safe_int(request.form.get("data_science"))

        total_score = (science + math + english + data_science) / 4
    else:
        return render_template("getResult.html")

    return redirect(url_for("success", score=total_score))









if __name__ == "__main__":
    app.run(debug=True)

