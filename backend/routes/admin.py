from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User  
from ..models import db

admin_bp = Blueprint('auth', __name__)

@admin_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usertype = request.form.get('usertype')
        email = request.form.get('email')
        password = request.form.get('password')
        secretkey = request.form.get('secretkey')

        ADMIN_SECRET = "mysecret123"

        # Validate fields
        if not email or not password or not usertype:
            flash("Please fill all required fields", "warning")
            return redirect(url_for('auth.register'))

        # Admin must give correct secret key
        if usertype == "admin":
            if secretkey != ADMIN_SECRET:
                flash("Invalid Admin Secret Key!", "danger")
                return redirect(url_for('auth.register'))

        # Check if email exists
        existing = User.query.filter_by(email=email).first()
        if existing:
            flash("Email already registered!", "warning")
            return redirect(url_for('auth.register'))

        # Save new user
        hashed_pw = generate_password_hash(password)
        new_user = User(email=email, password=hashed_pw, usertype=usertype)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please login.", "success")
        return redirect(url_for('auth.login'))

    return render_template("register.html")
@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usertype = request.form.get('usertype')
        email = request.form.get('email')
        password = request.form.get('password')
        secretkey = request.form.get('secretkey')

        ADMIN_SECRET = "mysecret123"

        if not email or not password:
            flash("Please enter email and password.", "warning")
            return redirect(url_for('auth.login'))

        # Fetch user
        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            flash("Invalid email or password!", "danger")
            return redirect(url_for('auth.login'))

        # -------- ADMIN LOGIN --------
        if usertype == "admin":

            if user.usertype != "admin":
                flash("You are not registered as an admin!", "danger")
                return redirect(url_for('auth.login'))

            if secretkey != ADMIN_SECRET:
                flash("Invalid Admin Secret Key!", "danger")
                return redirect(url_for('auth.login'))

            session['user_id'] = user.userid
            session['role'] = "admin"
            session['email'] = user.email

            flash("Logged in successfully as Admin!", "success")
            return redirect(url_for('search.dashboard'))

        # -------- NORMAL USER LOGIN --------
        session['user_id'] = user.userid
        session['role'] = "user"
        session['email'] = user.email

        flash(f"Welcome {user.email}!", "success")
        return redirect(url_for('search.home'))

    return render_template("login.html")
