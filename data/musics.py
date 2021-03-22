
from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy import orm


class Music(SqlAlchemyBase):
    __tablename__ = 'musics'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    file_path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    playlists = orm.relation('Playlist',
                          secondary='association_playlist_to_music',
                          back_populates='musics')