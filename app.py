from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Forside")

@app.route("/meny")
def meny():
    return render_template("menu.html")

@app.route("/varer")
def varer():
    return render_template("varer.html", title="Varer")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", title="Kontakt")

if __name__ == "__main__":
    app.run(debug=True)
