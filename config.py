import os
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.environ.get('MASTER_USER')
DB_PASSWORD = os.environ.get('MASTER_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = 'envtracker'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + DB_NAME

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME

SQLALCHEMY_TRACK_MODIFICATIONS = True
