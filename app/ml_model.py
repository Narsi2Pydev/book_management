from sqlalchemy.future import select
from app.models import Book

async def recommend_books(db_session, genre: str):
    result = await db_session.execute(select(Book).filter(Book.genre == genre).order_by(Book.average_rating.desc()))
    return result.scalars().all()
