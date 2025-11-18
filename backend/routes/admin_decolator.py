from functools import wraps
from flask import session, redirect, url_for, flash

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get("role") != "admin":
            flash("Admin access required!", "danger")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return wrapper
