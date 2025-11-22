from flask import render_template, session,url_for,jsonify,redirect, Blueprint,flash,request,g
from ..extentions import db
import re
from ..models import User
from ..models import Internship
from ..models import Training
from ..models import SearchHistory



Internship_bp = Blueprint('internship',__name__, url_prefix='/internship')

@Internship_bp.route('/addinternship', methods=['POST','GET']) #done
def add_internship():
    if request.method=='POST':
        title = request.form.get('title')
        provider= request.form.get('provider')
        location = request.form.get('location')
        salary = request.form.get('salary')
        posted_at = request.form.get('posted_at')
        link = request.form.get('link')

        
        try:
            newinternship = Internship(title=title,provider=provider,location=location,salary=salary,posted_at=posted_at,link =link)
            #newinternship.userid = g.user_id
            db.session.add(newinternship)
            db.session.commit()
            flash('internship added successfully!!','success')
            return redirect(url_for('internship.display_all'))
        except Exception as e:
            flash(f'unexpected error occured: {e}', 'danger')
            return redirect(url_for('internship.display_all'))
    return render_template('dashboard.html')
    
@Internship_bp.route('/delete/<int:id>',methods=['DELETE']) #done
def delete_internship(id):
    internship = db.session.query(Internship).filter(Internship.internship_id==id).first()
    try:
        if internship:
            db.session.delete(internship)
            db.session.commit()
            flash('internship deleted successfully' 'success')
            return redirect(url_for('internship.display_all'))
    except Exception as e:
        db.session.rollback()
        flash(f'unexpected error occured!!: {e}','danger')
        return redirect(url_for('internship.display_all'))


@Internship_bp.route('/displayall',methods=['GET'])
def display_all():
    adminDashboard = db.session.query(Internship).all()
    return render_template('internship.html',adminDashboard=adminDashboard)




