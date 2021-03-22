from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy import orm, Integer, ForeignKey

association_table_2 = sqlalchemy.Table('association_playlist_to_music', SqlAlchemyBase.metadata,
                                       sqlalchemy.Column('playlists', sqlalchemy.Integer,
                                                         sqlalchemy.ForeignKey('playlists.id')),
                                       sqlalchemy.Column('musics', sqlalchemy.Integer,
                                                         sqlalchemy.ForeignKey('musics.id')),
                                       )


class Playlist(SqlAlchemyBase):
    __tablename__ = 'playlists'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_id = sqlalchemy.Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='playlists')
    musics = orm.relation('Music',
                          secondary='association_playlist_to_music',
                          back_populates='playlists')
