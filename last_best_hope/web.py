from . import models, ejson, api
from flask import Flask, render_template, request

app = application = Flask(__name__)
app.json_encoder = ejson.Encoder
app.register_blueprint(api.blueprint, url_prefix="/api")

@app.route("/", methods=["GET"])
def get_index():
    return render_template("app/index.html")
