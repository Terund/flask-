import os

BASE_DIE = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    # 数据库地址sqlite
    # SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIE, "ORM.sqlite")
    # 数据库MySql
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/flaskblog"
    # 请求结束后自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 跟踪修改
    SQLALCHEMY_TRACK_MODIFICATION = True


class RunConfig:
    DEBUG = False


