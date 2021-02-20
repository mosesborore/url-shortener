from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def create_app():
	app = Flask(__name__)

	app.config['SECRET_KEY'] = 'urlshortner'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@hostname:port/databasename"
	app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://borore:borore1234@localhost:5432/urlmanager"

	db.init_app(app)

	from .models import UrlData
	create_db(app)

	from .views import views
	from .redirection import origin


	app.register_blueprint(views, url_prefix='')
	app.register_blueprint(origin, url_prefix='/s/')



	return app


def create_db(app):
	db.create_all(app=app)