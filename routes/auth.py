from flask import Blueprint, request, jsonify
from app.database import get_session
from app.auth import authenticate_user
from app.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
async def login():
    data = request.json
    session = await get_session()
    user = await authenticate_user(session, data["username"], data["password"])
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    # Generate a token here (simplified for demonstration purposes)
    token = f"token_for_{user.username}"
    return jsonify({"token": token})

@auth_bp.route("/register", methods=["POST"])
async def register():
    data = request.json
    session = await get_session()
    hashed_password = get_password_hash(data['password'])
    user = User(
        username=data['username'],
        hashed_password=hashed_password
    )
    created_user = await create_user(session, user)
    return jsonify({"id": created_user.id, "username": created_user.username})
