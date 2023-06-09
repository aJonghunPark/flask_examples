import os
from pathlib import Path

basedir = Path(__file__).parent.parent

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
hostname = os.environ.get("HOSTNAME")
database = os.environ.get("DATABASE")
db_url = f"mysql+mysqldb://{username}:{password}@{hostname}/{database}"


class BaseConfig:
    SECRET_KEY = "theiDah6wiez9meeboh3sobaeNg3Uquu"
    GOOGLE_CLIENT_ID = os.environ.get("OAUTH_GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("OAUTH_GOOGLE_CLIENT_SECRET")
    PUBLIC_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")
    SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")


# BaseConfigクラスを継承してLocalConfigクラスを作成する
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# BaseConfigクラスを継承してTestingConfigクラスを作成する
class TestingConfig(BaseConfig):
    db_url = "mysql+mysqldb://root:@localhost/flask_example_test"
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    TESTING = True


# config辞書にマッピングする
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
