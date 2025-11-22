from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User  
from ..models import db

admin_bp = Blueprint('adminauth', __name__)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        secretkey = request.form.get('secretkey')

        ADMIN_SECRET = "mysecret123"

        if not email or not password:
            flash("Please enter email and password.", "warning")
            return redirect(url_for('adminauth.login'))

        #fetch user data
        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            flash("Invalid email or password!", "danger")
            return redirect(url_for('adminauth.login'))

        # -- admin login ---#


        if secretkey != ADMIN_SECRET:
            flash("Invalid Admin Secret Key!", "danger")
            return redirect(url_for('adminauth.login'))

        session['user_id'] = user.userid
        session['role'] = "admin"
        session['email'] = user.email

        flash("Logged in successfully as Admin!", "success")
        return redirect(url_for('search.dashboard') )

    return render_template("adminlogin.html")
