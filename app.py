from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, Flask, render_template
from flask_login import LoginManager

from config import Config



# def create_app():

app = Flask(__name__)

db = SQLAlchemy(app)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.login_view = 'login.login'
login_manager.login_message = "ログインしてください"
login_manager.init_app(app)

from models.models import user_info
@login_manager.user_loader
def load_user(account_id):
     # since the user_id is just the primary key of our user table, use it in the query for the user
     return user_info.query.get(account_id)

from views.login import login_blueprint
app.register_blueprint(login_blueprint)
from views.dashboard import dashboard_blueprint
app.register_blueprint(dashboard_blueprint)
  

if __name__ == "__main__":
    app.run(debug=True)