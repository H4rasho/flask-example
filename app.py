from flask import Flask, request
from src.users.service import findAll, create, findById, delete, update
from src.database.main import init_db, db_session

init_db()

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.get("/users/")
def getUsers():
    return findAll()

@app.get("/users/<id>")
def getUser(id):
    return findById(id)

@app.post("/users/")
def createUser():
    movie = request.get_json()
    return create(movie.get("name"), movie.get("email"))

@app.delete("/users/<id>")
def deleteUser(id):
    return delete(id)

@app.put("/users")
def updateUser():
    movie = request.get_json()
    return update(movie.get("id"), movie.get("name"), movie.get("email"))

