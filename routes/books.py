from flask import Blueprint, jsonify, request
from app.database import get_session
from app.crud import get_book, create_book, update_book, delete_book
from app.ml_model import recommend_books
from app.summary_generator import generate_summary
from app.models import Book
from sqlalchemy.future import select

books_bp = Blueprint("books", __name__)

@books_bp.route("/", methods=["POST"])
async def create_new_book():
    data = request.json
    session = await get_session()
    summary = await generate_summary(data['content'])
    book = Book(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        summary=summary
    )
    created_book = await create_book(session, book)
    return jsonify(created_book)

@books_bp.route("/", methods=["GET"])
async def get_all_books():
    session = await get_session()
    result = await session.execute(select(Book))
    books = result.scalars().all()
    return jsonify(books)

@books_bp.route("/<int:book_id>", methods=["GET"])
async def get_book_by_id(book_id: int):
    session = await get_session()
    book = await get_book(session, book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    return jsonify(book)

@books_bp.route("/<int:book_id>", methods=["PUT"])
async def update_book_details(book_id: int):
    data = request.json
    session = await get_session()
    book = await get_book(session, book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    updated_book = await update_book(session, book, data)
    return jsonify(updated_book)

@books_bp.route("/<int:book_id>", methods=["DELETE"])
async def remove_book(book_id: int):
    session = await get_session()
    book = await get_book(session, book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    await delete_book(session, book)
    return jsonify({"message": "Book deleted"})

@books_bp.route("/recommendations/", methods=["GET"])
async def get_book_recommendations():
    genre = request.args.get('genre')
    session = await get_session()
    recommended_books = await recommend_books(session, genre)
    return jsonify(recommended_books)

@books_bp.route('/recommend/<string:title>', methods=['GET'])
async def recommend_books_route(title):
    try:
        recommended_books = recommend_books(title)
        return jsonify({
            'title': title,
            'recommended_books': recommended_books
        }), 200
    except IndexError:
        return jsonify({'message': 'Book not found'}), 404


@books_bp.route('/generate-summary', methods=['POST'])
def generate_summary_route():
    data = request.json
    book_text = data.get("book_text", "")

    if not book_text:
        return jsonify({"error": "Book content not provided"}), 400

    # Generate the summary using the function defined earlier
    summary = generate_summary(book_text)

    return jsonify({"summary": summary}), 200


