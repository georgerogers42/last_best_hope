from . import models, ejson, api
from flask import Flask, render_template, request

app = application = Flask(__name__)
app.json_encoder = ejson.Encoder
app.register_blueprint(api.blueprint, url_prefix="/api")

@app.route("/", methods=["GET"])
def get_index():
    with models.session() as s:
        page = s.query(models.Page).filter("index" == models.Page.slug).first()
        return render_template("app/index.html", page=page)
