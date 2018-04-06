import arrow
from . import models, ejson, api
from flask import Flask, render_template, request, redirect, url_for

app = application = Flask(__name__)
app.json_encoder = ejson.Encoder
app.register_blueprint(api.blueprint, url_prefix="/api")

def page_by_slug(s, slug):
    page = s.query(models.Page).filter(slug == models.Page.slug).first()
    if page == None:
        page = models.Page(slug=slug, title=slug, contents="", utime=arrow.get().datetime)
    return page

@app.route("/", methods=["GET"])
def get_index():
    return get_page("index")

@app.route("/page/<path:slug>", methods=["GET"])
def get_page(slug):
    with models.session() as s:
        page = page_by_slug(s, slug)
        return render_template("app/index.html", page=page)

@app.route("/edit/page/<path:slug>", methods=["GET"])
def get_page_form(slug):
    with models.session() as s:
        page = page_by_slug(s, slug)
        return render_template("app/edit.html", page=page)

@app.route("/edit/page/<path:slug>", methods=["POST"])
def post_page_form(slug):
    with models.session() as s:
        page = s.query(models.Page).filter(slug == models.Page.slug).first()
        if page == None:
            page = models.Page(slug=slug)
            s.add(page)
        page.title = request.form["title"]
        page.contents = request.form["contents"]
        page.arrow_utime = arrow.get()
    return redirect(url_for("get_page", slug=slug))
