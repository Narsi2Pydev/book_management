from sqlalchemy.future import select
from app.models import Book, User, Review

async def get_book(db_session, book_id: int):
    result = await db_session.execute(select(Book).filter(Book.id == book_id))
    return result.scalars().first()

async def create_book(db_session, book: Book):
    db_session.add(book)
    await db_session.commit()
    await db_session.refresh(book)
    return book

async def update_book(db_session, book: Book, updates: dict):
    for key, value in updates.items():
        setattr(book, key, value)
    await db_session.commit()
    await db_session.refresh(book)
    return book

async def delete_book(db_session, book: Book):
    await db_session.delete(book)
    await db_session.commit()

async def get_user_by_username(db_session, username: str):
    result = await db_session.execute(select(username).filter(User.username == username))
    return result.scalars().first()

#from app.crud import create_user, get_user_by_id, update_user, delete_user

async def get_user_by_id(db_session, user_id: int):
    result = await db_session.execute(select(Book).filter(User.user_id == user_id))
    return result.scalars().first()

async def create_user(db_session, user: User):
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    return user

async def update_user(db_session, user: User, updates: dict):
    for key, value in updates.items():
        setattr(user, key, value)
    await db_session.commit()
    await db_session.refresh(user)
    return user

async def delete_user(db_session, user: User):
    await db_session.delete(user)
    await db_session.commit()