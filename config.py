import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'KeepItSimpleStupid'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'blend_and_filter.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['nspnr18@gmail.com']

    YELP_API_KEY = "jgAIlOyDcteIC-QzduVUg5N-PgCgKcM5_Oi2F_gp0KYCE5xSwxGftWhWdby7QTMsJ0ihq9EVXqxP7zS7nwp5wV2xZ6Eyt2iRtr0ustfVipE8ZEdL4RCpZYQMmj6mYXYx"