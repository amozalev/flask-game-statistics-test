from flask import request, render_template, redirect, url_for, g, flash, session
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from app.api.models import *
from . import auth
from .forms import LoginForm
from app import login_manager
import config


@auth.before_request
def before_request():
    g.user = current_user


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    next = request.args.get('next')

    # pw_hash = generate_password_hash('0000')
    # print(pw_hash)

    if current_user.is_authenticated:
        return redirect(next or url_for('monitoring.show_device_data', device_id=session['min_device_id']))
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.name == request.form['login']).first()
        password = request.form['password']

        if user and check_password_hash(user.hash, password):
            user.authenticated = True
            login_user(user, user.hash)
            return redirect(next or url_for('api.index'))
        else:
            flash('Неправильные данные')
    return render_template("login.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    return redirect(url_for('auth.login'))
