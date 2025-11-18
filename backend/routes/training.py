from flask import render_template, session,url_for,jsonify,redirect, Blueprint,flash,request,g
import re
from ..models import User
from ..models import Internship
from ..models import Training
from ..models import SearchHistory
from ..extentions import db


Training_bp = Blueprint('training',__name__, url_prefix='/training')

@Training_bp.route('/addtraining', methods=['POST','GET']) #done
def add_training():
    if request.method=='POST':
        title = request.form.get('title')
        provider= request.form.get('provider')
        location = request.form.get('location')
        level = request.form.get('level ')
        posted_at = request.form.get('posted_at')
        paid_free = request.form.get('paid_free')
        link = request.form.get('link')

        
        try:
            newtraining = Training(title=title,provider=provider,location=location,level =level,paid_free =paid_free,posted_at=posted_at,link =link)
            db.session.add(newtraining)
            db.session.commit()
            flash('training added successfully!!','success')
            return redirect(url_for('training.display_all'))
        except Exception as e:
            flash(f'unexpected error occured: {e}', 'danger')
            return redirect(url_for('training.display_all'))
    return render_template('dashboard.html')

@Training_bp.route('/delete/<int:id>',methods=['DELETE']) #done
def delete_training(id):
    training = db.session.query(Training).filter(Training.trainingid==id).first()
    try:
        if training:
            db.session.delete(training)
            db.session.commit()
            flash('training deleted successfully' 'success')
            return redirect(url_for('training.display_all'))
    except Exception as e:
        db.session.rollback()
        flash(f'unexpected error occured!!: {e}','danger')


@Training_bp.route('/displayall',methods=['GET'])
def display_all():
    adminDashboard = db.session.query(Training).all()
    return render_template('dashboard.html',adminDashboard=adminDashboard)