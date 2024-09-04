from flask import request, jsonify
from passlib.context import CryptContext
from app.models import User
from sqlalchemy.future import select
from app.crud import get_user_by_username

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def authenticate_user(db_session, username: str, password: str):
    user = await get_user_by_username(db_session, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def requires_auth(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Authentication required"}), 401
        # Implement token validation logic here
        return func(*args, **kwargs)
    return wrapper
