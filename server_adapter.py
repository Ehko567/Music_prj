from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from sqlalchemy import sql
from werkzeug.security import generate_password_hash, check_password_hash

from data import db_session
from data.login_form import LoginForm
from data.reg_form import RegForm
from data.musics import Music
from data.users import User
from data.playlists import Playlist

app = Flask(__name__)
app.config['SECRET_KEY'] = '423h1g5kgjh12fj43gf5h3524u5g43u52ug54iy26g58fd5g98d5g8fd5g98d5gxbh7gdfhcht7wnr0d8f7qd3'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = User()
        user.login = form.login.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect('/login')
    return render_template('base.html')

@app.route('/test')
def test():
    return render_template('base.html')

def main():
    db_session.global_init('db/music_db.db')
    app.run()


if __name__ == '__main__':
    main()

