from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/maps')
def maps():
    return render_template("map_page.html")


@app.route('/agenda')
def agenda():
    return render_template("agenda.html")


@app.route('/materials')
def materials():
    return render_template("materials.html")


@app.route('/myspace-arielle')
def myspace_arielle():
    return render_template("index_arielle.html")


@app.route('/myspace-stephanie')
def myspace_stephanie():
    return render_template("index_stephanie.html")


if __name__ == "__main__":
    app.run(debug=True)
