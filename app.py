from flask import Flask, session, g
import config
from exts import db, mail
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from blueprints.chatbot import bp as chatbot_bp
from models import UserModel
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定配置文件
# 不使用之前的sqlalchemy导入
app.config.from_object(config)

# 初始化而不产生关联,将app传入外部配置进行初始化
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

# 产生关联，即对蓝图进行注册
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(chatbot_bp)


# blueprint：用来做模块化的
# 电影、读书、音乐、others

# before_request/before_first_request/after_first_request,等钩子函数，即在正常执行流程中的优先执行函数。
# hook,在执行主任务之前，获取用户的信息，用户的信息存储在session中，从session中获取用户信息为全局变量，后面传给其他地方
@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


@app.context_processor
def my_context_processor():
    return {"user": g.user}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
