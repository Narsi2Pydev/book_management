from flask import Blueprint, request, jsonify
from app.database import get_session
from app.models import User
from app.crud import create_user, get_user_by_id, update_user, delete_user
from app.auth import get_password_hash, requires_auth

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["POST"])
async def create_new_user():
    data = request.json
    session = await get_session()
    hashed_password = get_password_hash(data['password'])
    user = User(
        username=data['username'],
        hashed_password=hashed_password
    )
    created_user = await create_user(session, user)
    return jsonify({"id": created_user.id, "username": created_user.username})

@users_bp.route("/<int:user_id>", methods=["GET"])
@requires_auth
async def get_user(user_id: int):
    session = await get_session()
    user = await get_user_by_id(session, user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"id": user.id, "username": user.username})

@users_bp.route("/<int:user_id>", methods=["PUT"])
@requires_auth
async def update_user_details(user_id: int):
    data = request.json
    session = await get_session()
    user = await get_user_by_id(session, user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    if "password" in data:
        data["hashed_password"] = get_password_hash(data.pop("password"))
    updated_user = await update_user(session, user, data)
    return jsonify({"id": updated_user.id, "username": updated_user.username})

@users_bp.route("/<int:user_id>", methods=["DELETE"])
@requires_auth
async def delete_user(user_id: int):
    session = await get_session()
    user = await get_user_by_id(session, user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    await delete_user(session, user)
    return jsonify({"message": "User deleted"})
