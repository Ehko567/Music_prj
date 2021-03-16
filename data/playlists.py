from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy import orm


class Playlist(SqlAlchemyBase):
    __tablename__ = 'playlists'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    list_of_music_ids = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    owner_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)