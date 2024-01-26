from flask import Flask, redirect,  render_template, url_for, request
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from sqlalchemy.orm import load_only

from models import db, init_app, Todos

# Helper functions to render a complete or incomplete todo, kinda using these as 'components' a la React in a sense.
from renders import render_complete_todo, render_incomplete_todo

# Flask app
app = Flask(__name__)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
init_app(app)


# Flask migration
Migrate(app, db, compare_type=True)


# Comment out below if running
# `flask db init` for the first time
with app.app_context():
  upgrade()

# Here's the route concept! The homepage should only take a 'GET' request
# and just display the content, while the others are mostly 'POST' requests
# to handle sending data to the server.
@app.route("/", methods=["GET"])
def index():

  # Get all the todos currently
  todos = db.session.execute(db.select(Todos)).scalars().all()

  # Use them to render template
  return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():

  # Create new todo
  todo = Todos (
    title = request.form.get("title"),
    details = request.form.get("details"),
    complete = False
  )

  # Add to session and commit
  db.session.add(todo)
  db.session.commit()

  # Send back resulting todo item
  return render_incomplete_todo(todo)


@app.route("/complete", methods=["POST"])
def mark_complete():

  # Update todo in db
  todo_id = request.form.get("complete")
  todo = db.session.execute(db.select(Todos).where(Todos.id==todo_id)).scalar()
  todo.complete = not todo.complete
  db.session.commit()

  # Send back appropriate HTML element
  if todo.complete:
    return render_complete_todo(todo)
  else:
    return render_incomplete_todo(todo)

@app.route("/remove", methods=["POST"])
def remove():

  # Get the id of the todo to remove from the button and delete
  todo_id = request.form.get("remove")
  todo = db.session.execute(db.select(Todos).where(Todos.id==todo_id)).scalar()
  db.session.delete(todo)
  db.session.commit()

  # Send back an empty string to replace the element.
  # NOTE: Could just use the hx-delete route and ignore returning anything, this is mostly just to allow error checking (which I'm not currently doing,
  # but in case I checked the transaction worked fine, otherwise I guess I would return back the same element to replace itself with itself, which
  # seems kinda scuffed but I don't know how else this works in HTMX, first time ever using it).
  return ""