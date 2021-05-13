from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def create_app():
	app = Flask(__name__, instance_relative_config=True)

	# LOAD CONFIGATIONS from instance/config.py
	app.config.from_pyfile("config.py")
	db.init_app(app)


	from .views import views
	from .redirection import origin

	with app.app_context():
		db.create_all()


	app.register_blueprint(views, url_prefix='')
	app.register_blueprint(origin, url_prefix='/')

	# with app.app_context():
	# 	# create the database IF NOT EXISTS
	# 	db.create_all()

	return app
