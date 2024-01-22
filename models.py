from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
  db.init_app(app)

class Todos(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(64), nullable=False)
  details = db.Column(db.String(512), nullable=True)
  complete = db.Column(db.Boolean, nullable=False)