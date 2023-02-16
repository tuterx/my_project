# 配置数据库
# mysql所在的主机名
HOSTNAME = "127.0.0.1"
# MYSQL监听的端口号，默认3306
PORT = 3306
# 链接mysql的用户名，读者用自己设置的
USERNAME = "root"
# 连接mysql的密码，读者用自己的
PASSWORD = "xlx8246579"
# mysql连接的数据库名称
DATABASE = "fake_zhihu"

DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URL

# 长约20个字符的随机字符串
SECRET_KEY = "asdfasdfjasdfjasd;lf"

MAIL_SERVER = "smtp.163.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "xlx18856967520@163.com"
MAIL_PASSWORD = "NGKYNFBRAMRFNQEN"
MAIL_DEFAULT_SENDER = "xlx18856967520@163.com"


MY_CHATBOT_API_KEY = "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"