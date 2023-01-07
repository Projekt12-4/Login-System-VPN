import uuid
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import bleach

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Cleaning user input
        email = bleach.clean(email)
        password = bleach.clean(password)

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout() -> redirect:
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up() -> render_template    :
    if request.method == 'POST':
        email: str = request.form.get('email')
        first_name: str = request.form.get('firstName')
        password1: str = request.form.get('password1')
        password2: str = request.form.get('password2')
        u_uid: str = uuid.uuid5(namespace=uuid.NAMESPACE_OID, name="AUTH")
        u_uid = str(u_uid)
        # Cleaning user input on sign-up
        email = bleach.clean(email)
        first_name = bleach.clean(first_name)
        password1 = bleach.clean(password1)
        password2 = bleach.clean(password2)

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:

            # Wireguard part
            server = Server('my-test-server', '192.168.178.0/24', address='0.0.0.0')

            # Write out the server config to the default location: /etc/wireguard/wg0.conf
            server.config().write()
        
            peer = server.peer()
            print(peer)
            # Output this peer's config for copying to the peer device
            kfile: str = peer.config().local_config


            # Rewrite the server config file including the newly created peer
            server.config().write()
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
            password1, method='sha256'), uid=u_uid, key_file=kfile)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
