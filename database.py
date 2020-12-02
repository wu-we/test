from flask_sqlalchemy import SQLAlchemy
from config import Config
db = SQLAlchemy()
# アプリでDB操作を行えるように初期設定する
def init_db(app):
  app.config.from_object(Config)
  db.init_app(app)