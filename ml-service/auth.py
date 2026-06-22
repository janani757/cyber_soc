from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import User
from database import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    user = User(
        username=data["username"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role=data.get("role", "analyst")
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"})


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid password"}), 401

    token = create_access_token(
        identity={
            "email": user.email,
            "role": user.role
        }
    )

    return jsonify({
        "token": token,
        "role": user.role
    })