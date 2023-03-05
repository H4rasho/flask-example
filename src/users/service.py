from src.database.main import db_session
from src.users.model import User
from flask import jsonify

def findAll():
   users = User.query.all()
   serialze = []
   for user in users:
      serialze.append({
         "id": user.id,
         "name": user.name,
      })
   return jsonify(serialze)


def create(name, email):
   user = User(name, email)
   db_session.add(user)
   db_session.commit()
   serialze = {
      "id": user.id,
      "name": user.name,
   }
   return jsonify(serialze)


def findById(id):
   user = User.query.get(id)
   serialze = {
      "id": user.id,
      "name": user.name,
   }
   return jsonify(serialze)

def delete(id):
   user = User.query.get(id)
   if not user:
      return jsonify({"message": "User not found"})
   db_session.delete(user)
   db_session.commit()
   return jsonify({"message": "User deleted successfully"})


def update(id, name, email):
   user = User.query.get(id)
   if not user:
      return jsonify({"message": "User not found"})
   user.name = name
   user.email = email
   db_session.commit()
   serialze = {
      "id": user.id,
      "name": user.name,
   }
   return jsonify(serialze)

