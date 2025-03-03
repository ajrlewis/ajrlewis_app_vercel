import datetime
import os
import secrets

from dotenv import load_dotenv

load_dotenv()


class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = False
    # # SQLALCHEMY_ECHO = True

    JSON_SORT_KEYS = False

    # MAIL_SERVER = os.getenv("MAIL_SERVER")
    # MAIL_PORT = os.getenv("MAIL_PORT")
    # MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    # MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    # MAIL_DEFAULT_SENDER_NAME = os.getenv("MAIL_DEFAULT_SENDER_NAME")
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True

    # REMEMBER_COOKIE_DURATION = datetime.timedelta(
    #     seconds=int(os.getenv("REMEMBER_COOKIE_DURATION", 600))
    # )
    # PERMANENT_SESSION_LIFETIME = REMEMBER_COOKIE_DURATION

    SECRET_KEY = secrets.token_urlsafe(32)
