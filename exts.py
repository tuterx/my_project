# exts.py这个文件存在的意义是为了解决循环引用的问题
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()

mail = Mail()
