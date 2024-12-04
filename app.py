from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
# dekorátor - upraví zlepší funkci
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    py_var = request.args.get("html_formname") 
    return render_template ("form.html", jinjja_var=py_var)


if __name__ == "__main__": 
    app.run(debug=True) #spouštění flaskové aplikace