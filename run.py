from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/maps')
def maps():
    return render_template("map_page.html")

@app.route('/maps-plain')
def plain_map():
    return render_template("Free_map_open_city.html")


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

@app.route('/contact')
def contact_page():
    return render_template("contact_page.html")

@app.route('/omnis')
def omni():
    return render_template("graphics_omni.html")

@app.route('/omnis-plain')
def plain_omni_graphic():
    return render_template("graphics_omni_plain.html")

@app.route('/regions')
def region():
    return render_template("graphics_region.html")


@app.route('/regions-plain')
def plain_region_graphic():
    return render_template("graphics_region_plain.html")


if __name__ == "__main__":
    app.run(debug=True)
