class Config(object):
    #Database Configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY= 'Your Key'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234567890@localhost/hayabusa-survey"