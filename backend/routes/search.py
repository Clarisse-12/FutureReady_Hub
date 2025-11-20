import flask
from flask import render_template,redirect,url_for,Blueprint
from ..middleware import login_required
from ..models import Internship, Training


from ..extentions import db

search_bp=Blueprint('search',__name__)
@login_required
@search_bp.route('/search',methods=['GET'])
def search():
    internship=db.session.query(Internship).all()
    training=db.session.query(Training).all()
    return render_template('search.html', internship=internship, training=training)

@login_required
@search_bp.route('/resource',methods=['GET'])
def resource():
    return render_template('resource.html')

@search_bp.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')


@search_bp.route('/home',methods=['GET'])
def home():
    return render_template('home.html')

@search_bp.route('/index',methods=['GET'])
def index():
    return render_template('index.html')


@search_bp.route('/dashboard',methods=['GET'])
def dashboard():
    return render_template('dashboard.html')



@search_bp.route('/resources')
def resources():
    return render_template('resources.html')
@search_bp.route('/selectlogin',methods=['GET'])
def select():
    return render_template('select_login.html')




