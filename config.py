from logging import DEBUG
import os
from dotenv import load_dotenv

load_dotenv()


class config:
    SERVER_NAME = "http://127.0.0.1.5000/"
    DEBUG = True

    DATABASE_PATH = "application/database/test.db"
    DB_TOKEN = os.environ.get("DB_TOKEN", "")
    ENCRYPT_DB = True

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/statics/"
