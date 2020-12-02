from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user, login_required
from models.models import user_info
login_blueprint = Blueprint('login', __name__)


@login_blueprint.route('/hayabusa/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET': 
        return render_template('login/login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        if not email and not password:
            flash('メールアドレスとパスワードを入力してください。')
            flash("emptyError")
            return render_template('login/login.html')
        elif not email:
            flash('メールアドレスを入力してください。')
            flash("emailError")
            return render_template('login/login.html')
        elif not password:
            flash('パスワードを入力してください。')
            flash("passwordError")
            return render_template('login/login.html')
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        user = user_info.query.filter_by(email=email).first()
        if not user or user.password != password:
        # or not check_password_hash(user.password, password):
            flash('メールアドレスかパスワードか間違えました')
            flash("loginError")
            return render_template('login/login.html') # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user)
        return redirect(url_for('dashboard.dashboard'))
        # return "ok"
 
# @login.route('/login', methods=["GET"])
# def login_get():
#     return render_template('login/login.html')
   
    
# @login.route('/signup')
# def signup():
#     return 'Signup'

@login_blueprint.route('/hayabusa/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login'))