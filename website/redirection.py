from flask import Blueprint, redirect
from . import db
from .models import UrlData

origin = Blueprint("origin", __name__)


@origin.route("/<short_url>")
def redirect_to_full_url(short_url):
    
    data = db.session.query(UrlData).filter_by(short_url=short_url).first_or_404(description="Not found. Check the url and try again")
    
    full_url = data.long_url

    # increment the click
    data.clicks += 1

    db.session.commit()

    return redirect(full_url)
