from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

association_table = sqlalchemy.Table('association', SqlAlchemyBase.metadata,
                                     sqlalchemy.Column('users', sqlalchemy.Integer,
                                                       sqlalchemy.ForeignKey('users.id')),
                                     sqlalchemy.Column('musics', sqlalchemy.Integer,
                                                       sqlalchemy.ForeignKey('musics.id')),
                                     )

association_user_to_playlist = sqlalchemy.Table('association_user_to_playlist', SqlAlchemyBase.metadata,
                                                sqlalchemy.Column('users', sqlalchemy.Integer,
                                                                  sqlalchemy.ForeignKey('users.id')),
                                                sqlalchemy.Column('playlists', sqlalchemy.Integer,
                                                                  sqlalchemy.ForeignKey('playlists.id')),
                                                )


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    list_of_music_ids = orm.relation("Music",
                                     secondary="association",
                                     backref="musics")
    login = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    playlists = relationship('Playlist')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
