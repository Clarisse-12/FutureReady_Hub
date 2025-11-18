import flask
from flask import render_template,redirect,url_for,Blueprint
from ..middleware import login_required


from ..extentions import db

search_bp=Blueprint('search',__name__)
@login_required
@search_bp.route('/search',methods=['GET'])
def search():
    return render_template('search.html')

@login_required
@search_bp.route('/resource',methods=['GET'])
def resource():
    return render_template('resource.html')


@login_required
@search_bp.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

@login_required
@search_bp.route('/home',methods=['GET'])
def home():
    return render_template('contact.html')

@login_required
@search_bp.route('/dashboard',methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


@login_required
@search_bp.route('/resources')
def resources():
    return render_template('resources.html')

