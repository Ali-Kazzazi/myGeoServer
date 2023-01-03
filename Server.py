from flask import Flask
from flask import render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return "<p>Hello, This is my GeoServer!</p>"

@app.route("/config")
def config():
    return "<p>This is config page!</p>"

@app.route('/about')
def about():
    return 'The about page'

@app.route('/map')
def map():
    return render_template('map.html')

if __name__ == "__main__":
    app.run()