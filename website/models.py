from . import db

class UrlData(db.Model):
	__tablename__ = 'url'

	url_id = db.Column(db.Integer, primary_key=True)
	long_url = db.Column(db.String(), nullable = False)
	short_url = db.Column(db.String(), nullable = True)
	clicks = db.Column(db.Integer(), nullable=False, default=0)


	def __init__(self, long_url):
		self.long_url = long_url