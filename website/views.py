from flask import Blueprint, render_template, request, url_for, redirect, flash
from .util import base62_decode, base62_encode
from .model import database

views = Blueprint('views', __name__, static_folder='static', template_folder='templates')


@views.route("/")
def index():
    return render_template("index.html")

@views.route("/shorten", methods=['GET', 'POST'])
def shorten_url():
    if request.method == "POST":
        full_url = request.form.get("fullURL")

        if full_url:
            # insert the url to the database
            database.insert_new_entry(full_url)

            # get the id for the new entry
            url_id = database.get_last_entry()['id']

            # encode the url_id to base62 equivalent
            # which is used as the short url version of
            # of the "full_url"
            short_url = base62_encode(url_id)

            # update the short_url column
            database.update_short_url(url_id, short_url)
        return render_template('index.html', data= short_url)
    return redirect(url_for('views.index'))


@views.route("/all")
def all_urls():
    data = {'all': []}

    data = {'all': []}

    for i in database.select_all():
        temp = {'id': i[0],
                'long_url': i[1],
                'short_url': i[2]}

        data['all'].append(temp)

    return render_template('all.html', data=data)