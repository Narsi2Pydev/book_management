from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from asgiref.wsgi import WsgiToAsgi

db = SQLAlchemy()

def init_db(app):
    engine = create_async_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    async_session = sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    app.async_session = async_session

    with app.app_context():
        db.init_app(app)
        db.create_all()

async def get_session(app):
    async with app.async_session() as session:
        yield session
