from flask import Blueprint, render_template, request, url_for, redirect, flash, jsonify
from .util import base62_decode, base62_encode
from . import db
from .models import UrlData


views = Blueprint('views', __name__, static_folder='static',
                  template_folder='templates')


@views.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form.get("fullURL")

        if long_url:
            new_url = UrlData(long_url=long_url)
            db.session.add(new_url)

            # get the last entry
            last_entry = db.session.query(UrlData).order_by().all()[-1]

            # get the id
            url_id = last_entry.url_id

            # get short_url using the url_id
            short_url = base62_encode(url_id)

            last_entry.short_url = short_url

            db.session.commit()
            return render_template('index.html', data=short_url)
    return render_template("index.html")


@views.route("/shorten", methods=['GET', 'POST'])
def shorten_url():

    return redirect(url_for('views.index'))


@views.route("/all")
def all_urls():
    urls = UrlData.query.all()

    data = {"all": []}

    count = 1
    for url in urls:
        curr = {"count": count, "long_url": url.long_url,
                "short_url": url.short_url, "clicks": url.clicks}

        count += 1
        data['all'].append(curr)

    return jsonify(data)
