
from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy import orm


class Music(SqlAlchemyBase):
    __tablename__ = 'musics'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    file_path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    owner_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)