import os

DB_USERNAME = "root" #os.environ.get('MASTER_USER')
DB_PASSWORD = "root" #os.environ.get('MASTER_PASSWORD')
DB_HOST = "localhost:3307/" #os.environ.get('DB_HOST')
DB_NAME = 'envtracker'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + DB_NAME
SQLALCHEMY_TRACK_MODIFICATIONS = True
