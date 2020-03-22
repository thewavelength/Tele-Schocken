import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))




class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'geheim'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:test@127.0.0.1:8889/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
