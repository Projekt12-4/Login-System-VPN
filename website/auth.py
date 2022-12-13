from uuid_extensions import uuid7str
from flask import Blueprint, render_template, request, flash, redirect, url_for
from passlib.hash import argon2
from flask_login import login_user, login_required, logout_user, current_user
import bleach
from . import db
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Cleaning user input
        email = bleach.clean(email)
        email = email.lower()
        password = bleach.clean(password)

        user = User.query.filter_by(email=email).first()
        if user:
            pass_verify: bool = argon2.verify(password, user.password)
            if pass_verify:
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
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Cleaning user input on sign-up
        email = bleach.clean(email)
        email = email.lower()
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
            # Vars for the database
            userid: str = uuid7str()
            hash_pass: str = str(argon2.hash(password1))

            new_user = User(
                uid = userid, 
                email=email, 
                first_name=first_name, 
                password=hash_pass # new hashing function (argon2)
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)



