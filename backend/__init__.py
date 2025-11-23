import sqlite3
import os
import flask
from flask import Flask, render_template,session,g
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes.search import search_bp
from .routes.internship import Internship_bp
from .routes.auth import auth_bp
from .routes.training import Training_bp
from .routes.admin import admin_bp
from .extentions import db




import sqlite3
from flask import Flask
from .extentions import db, migrate, init_extensions

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'testing'
    


    


    init_extensions(app)
    with app.app_context():
        db.create_all()
   
    
    from .models import User, Internship, Training, SearchHistory

 




    @app.before_request
    def load_user_id():
        user_id = session.get('user_id')
        email= session.get('email')
        if user_id == None:
            g.user_id = None
            g.email = None
        else:
            g.user_id = user_id
            g.email = email
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/admin')
    def admin_dashboard():
        return render_template('admin_dashboard.html')

    
    app.register_blueprint(search_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(Internship_bp)
    app.register_blueprint(Training_bp)
    app.register_blueprint(admin_bp)
    






    if test_config is None:
        #load instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        #test load config if pass
        app.config.from_mapping(test_config)

    #ensure folder exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


  