def render_incomplete_todo(todo):
  return f"""
        <div class="row todo-item" data-todo-id="1">
          <div class="col-3 d-flex justify-content-center">
            <b> {todo.title} </b>
          </div>
          <div class="col-6 d-flex justify-content-center">
            <p> {todo.details} </p>
          </div>
          <div class="col-2 d-flex justify-content-center">
            <div class="button-container">
              <button class="btn btn-success" value={todo.id} type="submit" name="complete" hx-post="/complete" hx-target="closest .todo-item" hx-swap="outerHTML">
                Complete
              </button>
              <button class="btn btn-danger" value={todo.id} type="submit" name="remove" hx-post="/remove" hx-target="closest .todo-item" hx-swap="outerHTML"> Remove </button>
            </div>
          </div>
        </div>
  """

def render_complete_todo(todo):
  return f"""
        <div class="row todo-item todo-complete" data-todo-id="1">
          <div class="col-3 d-flex justify-content-center">
            <b> {todo.title} </b>
          </div>
          <div class="col-6 d-flex justify-content-center">
            <p> {todo.details} </p>
          </div>
          <div class="col-2 d-flex justify-content-center">
            <div class="button-container">
              <button class="btn btn-warning" value={todo.id} type="submit" name="complete" hx-post="/complete" hx-target="closest .todo-item" hx-swap="outerHTML">
                Uncomplete
              </button>
              <button class="btn btn-danger" value={todo.id} type="submit" name="remove" hx-post="/remove" hx-target="closest .todo-item" hx-swap="outerHTML"> Remove </button>
            </div>
          </div>
        </div>
  """

