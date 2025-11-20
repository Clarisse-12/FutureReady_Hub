from flask import render_template, session,url_for,redirect, Blueprint,flash,request,g
from werkzeug.utils import secure_filename
from datetime   import datetime
import os
from backend.extentions import db
from sqlalchemy.exc import IntegrityError
from ..models import User



auth_bp = Blueprint('auth',__name__,url_prefix='/auth')
@auth_bp.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')


        if not password and not email:
            flash('you need to provide atleast email and password!', 'danger')
        user = db.session.query(User).filter_by(email=email).first()
        if user:
            flash('user already exist')
            return render_template('signup.html')
            
        try:
                
            newuser = User(email=email)
            newuser.set_hashpassword(password)
            db.session.add(newuser)
            db.session.commit()


            flash('you have registered successfully please login','success')
            return redirect(url_for('search.select'))
        except IntegrityError:
            db.session.rollback()
            flash('user already exist please login!!', 'warning')
        except Exception as e:
            flash(f'unexpected error occured: {e}','danger')
    return render_template('signup.html')


@auth_bp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        usertype=request.form.get('usertype')
        email = request.form.get('email')
        password = request.form.get('password')




        if not email and not password:
            flash('please provide your email and password before proceeding!!','info')
            return render_template('login.html')
        user = db.session.query(User).filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.userid
            session['email']=user.email
            flash(f'logged in successfully as {user.email}', 'success')
            return redirect(url_for('search.search'))
        flash('invalid email or password!! please check and try again!! or sig','danger')
        return render_template('index.html')
    return render_template('login.html')
@auth_bp.route('/logout')
def logout():
    session.pop('user_id',None)
    session.pop('email',None)
    flash('you have been logout successfully, you might want to login again','success')
    return render_template('index.html')