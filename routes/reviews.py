from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Review
from app.database import db
from utils.llama3_integration import generate_review_summary

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/', methods=['POST'])
@jwt_required()
def add_review():
    user_id = get_jwt_identity()
    data = request.json
    new_review = Review(
        book_id=data['book_id'],
        user_id=user_id,
        rating=data['rating'],
        review_text=data['review_text']
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully'}), 201

@reviews_bp.route('/<int:book_id>', methods=['GET'])
def get_reviews(book_id):
    reviews = Review.query.filter_by(book_id=book_id).all()
    return jsonify([{
        'user_id': review.user_id,
        'rating': review.rating,
        'review_text': review.review_text
    } for review in reviews]), 200

@reviews_bp.route('/summary/<int:book_id>', methods=['GET'])
def get_review_summary(book_id):
    reviews = Review.query.filter_by(book_id=book_id).all()
    review_texts = ' '.join([review.review_text for review in reviews])
    summary = generate_review_summary(review_texts)
    return jsonify({'summary': summary}), 200
