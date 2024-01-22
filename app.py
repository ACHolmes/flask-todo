from flask import Flask, redirect,  render_template, url_for, request
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from sqlalchemy.orm import load_only

from models import db, init_app, Todos

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

@app.route("/", methods=["GET"])
def index():

  query = db.select(Todos)
  todos = db.session.execute(query).scalars().all()
  # print(todos)
  # todos.map(lambda todo:
  #           f"""
  #   <tr>
  #     <th scope="row"> {todo.title} </th>
  #     <td> {todo.details} </td>
  #   </tr> """)

  # todos.join("")

  return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():

  todo = Todos (
    title = request.form.get("title"),
    details = request.form.get("details"),
    complete = False
  )

  db.session.add(todo)
  db.session.commit()
  # print(request.form)
  return f"""
      <div class="row todo-item" data-todo-id='{todo.id}'>
        <div class="col-1 d-flex justify-content-center">
          <input value={todo.id} type="checkbox" name="complete" hx-post="/complete" hx-target=".todo-item closest" hx-swap="innerHTML">
        </div>
        <div class="col-3 d-flex justify-content-center">
          <b>{ todo.title }</b>
        </div>
        <div class="col-6 d-flex justify-content-center">
          { todo.details }
        </div>
        <div class="col-2 d-flex justify-content-center">
          <button class="btn btn-danger"> Remove </button>
        </div>
      </div>      """


@app.route("/complete", methods=["POST"])
def mark_complete():
  todo_id = request.form.get("complete")
  print(f"todo id: {todo_id}")
  todo = db.session.execute(db.select(Todos).where(Todos.id==todo_id)).scalar()
  print(f"todo complete pre-update: {todo.complete}")
  todo.complete = not todo.complete
  db.session.commit()
  print(f"todo complete post-update: {todo.complete}")
  print(f"todo complete post-update: {todo.complete}")

  print(f"todo id: {todo.id}")
  print("---")
  # check = db.session.execute(db.select(Todos).where(Todos.id==todo_id)).scalar()
  if todo.complete:
    return f"""
        <div class="row todo-item" data-todo-id={todo.id}>
          <div class="col-1 d-flex justify-content-center">
            <input value={todo.id} type="checkbox" name="complete" hx-trigger="click" hx-post="/complete" hx-target="closest .todo-item" hx-swap="outerHTML" checked>
          </div>
          <div class="col-3 d-flex justify-content-center">
            <b> { todo.title } </b>
          </div>
          <div class="col-6 d-flex justify-content-center">
            { todo.details }
          </div>
          <div class="col-2 d-flex justify-content-center">
            <button class="btn btn-danger"> Remove </button>
          </div>
        </div>
  """
  else:
    return f"""
        <div class="row todo-item" data-todo-id={todo.id}>
          <div class="col-1 d-flex justify-content-center">
            <input value={todo.id} type="checkbox" name="complete" hx-trigger="click" hx-post="/complete" hx-target="closest .todo-item" hx-swap="outerHTML">
          </div>
          <div class="col-3 d-flex justify-content-center">
            <b> { todo.title } </b>
          </div>
          <div class="col-6 d-flex justify-content-center">
            { todo.details }
          </div>
          <div class="col-2 d-flex justify-content-center">
            <button class="btn btn-danger"> Remove </button>
          </div>
        </div>
  """