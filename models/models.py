from flask_login import UserMixin
from database import db
from sqlalchemy.dialects.mysql import TINYINT as Tinyint

class user_info(UserMixin, db.Model):
    account_id = db.Column(db.String(36), primary_key=True) # primary keys are required by SQLAlchemy
    login_id = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    telephone = db.Column(db.String(13))
    company_name = db.Column(db.String(255))
    line = db.Column(db.String(255))
    youtube = db.Column(db.String(255))
    ekiten = db.Column(db.String(255))
    google = db.Column(db.String(255))
    e_park = db.Column(db.String(255))
    parent_account_id = db.Column(db.String(36))
    deleted = db.Column(Tinyint(2))
    create_datetime = db.Column(db.DateTime)
    update_datetime = db.Column(db.DateTime)

    def __init__(self, account_id, login_id, password, email, telephone, 
                company_name, line, youtube, ekiten, google, e_park, parent_account_id, 
                deleted, create_datetime, update_datetime):

        self.account_id = account_id
        self.login_id = login_id
        self.password = password
        self.email = email
        self.telephone = telephone
        self.company_name = company_name
        self.line = line
        self.youtube = youtube
        self.ekiten = ekiten
        self.google = google
        self.e_park = e_park
        self.parent_account_id = parent_account_id
        self.deleted = deleted
        self.create_datetime = create_datetime
        self.update_datetime = update_datetime
        
    # def get_id(self):
    #     return self.account_id
    @property
    def id(self):
        return self.account_id


# class user_test(db.Model):
#     account_id = db.Column(db.String(36), primary_key=True) # primary keys are required by SQLAlchemy
#     login_id = db.Column(db.String(255))
#     password = db.Column(db.String(255))
#     email = db.Column(db.String(255))
    

# def __init__(self, account_id, login_id, password, email):

#     self.account_id = account_id
#     self.login_id = login_id
#     self.password = password
#     self.email = email
    
    