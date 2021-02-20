from flask import Blueprint, redirect
from .model import database

origin = Blueprint("origin", __name__)


@origin.route("/<short_url>")
def redirect_to_full_url(short_url):
    full_url = database.find_full_url(str(short_url))

    return redirect(full_url)
