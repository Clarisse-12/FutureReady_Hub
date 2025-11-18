from functools import wraps
from flask import flash, redirect, url_for, session

def login_required(f):
    @wraps(f)
    def decorated_function(*k, **ka):
        if 'user_id' not in session:
            flash('you need to login before accessing this','warning')
            return redirect(url_for('auth.login'))
        return f(k,*ka)

    return decorated_function

def Admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('usertype') != 'admin':
            flash('Access denied: Admins only.', 'danger')
            return redirect(url_for('search.home'))
        return f(*args, **kwargs)
    return decorated_function


def User_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('usertype') != 'user':
            flash('Access denied: Users only.', 'danger')
            return redirect(url_for('search.home'))
        return f(*args, **kwargs)
    return decorated_function