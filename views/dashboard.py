from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required

dashboard_blueprint = Blueprint('dashboard', __name__)

 
@dashboard_blueprint.route('/hayabusa/dashboard')
@login_required
def dashboard():
    return render_template('dashboard/dashboard.html')
   
