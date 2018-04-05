from . import models, ejson, api
from flask import Flask, render_template, request

app = application = Flask(__name__)
app.json_encoder = ejson.Encoder
app.register_blueprint(blueprint, url_prefix="/api")

