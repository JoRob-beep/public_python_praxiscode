from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

def validate_sign_up(email, first_name, password1, password2, company_number, phone, address):
    if User.query.filter_by(email=email).first():
        return 'Email existiert bereits.'
    if len(email) < 4:
        return 'Email muss länger als 3 Zeichen lang sein.'
    if len(first_name) < 2:
        return 'Name muss länger als 1 Zeichen lang sein.'
    if password1 != password2:
        return 'Passwörter stimmen nicht überein.'
    if len(password1) < 7:
        return 'Passwort muss länger als 7 Zeichen lang sein.'
    # Firmennummer, Telefon und Adresse können optional validiert werden
    return None

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Erfolgreich angemeldet!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.shop'))
        flash('Falsche Email oder falsches Passwort.', category='error')
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
        company_number = request.form.get('companyNumber')
        phone = request.form.get('phone')
        address = request.form.get('address')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        error_message = validate_sign_up(email, first_name, password1, password2, company_number, phone, address)
        if error_message:
            flash(error_message, category='error')
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                company_number=company_number,
                phone=phone,
                address=address,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account erstellt!', category='success')
            return redirect(url_for('views.shop'))
    return render_template("sign_up.html", user=current_user)


@auth.route('/category')
def category():
    return render_template("category.html")