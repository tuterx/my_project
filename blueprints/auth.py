from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from exts import mail, db
from flask_mail import Message
import string
import random
from models import EmailCaptchaModel
from .forms import RegisterForm, LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash
# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在!")
                return render_template("login.html")
            if check_password_hash(user.password, password):
                # cookie:
                # cookie中不适合存储太多的数据，只适合存储少量数据
                # cookie一般用来存放登录授权的东西
                # session服务器解决方案
                # flask中的session，是经过加密后存储在cookie中的,其中包含一些信息，如user_id
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误！")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
    return render_template("login.html")


# GET: 从服务器上获取数据
# POST： 将客户端数据提交到服务器
@bp.route("/register", methods=['POST', 'GET'])
def register():
    # 验证用户提交的邮箱和验证码是否对应且正确
    # 表单验证：flask-wtf: wtforms
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱功能测试", recipients=["317085711@qq.com"], body="the content is about a test")
    mail.send(message)
    return "测试邮箱发送成功！"


# bp.route: 如果没有指定的methods参数，默认就是GET请求
@bp.route("/captcha/email")
def get_email_captcha():
    # 传参类型：路径传参-/captcha/email/<email> 该方法需要在视图函数中传入参数
    # 类型二：/captcha/email?email=xxxx@qq.com 该方法可以直接从地址中获得而不传入
    email = request.args.get('email')
    # 4到6位的数字或字母组合
    source = string.digits * 6
    captcha = random.sample(source, 6)
    captcha = "".join(captcha)
    # I/O: Input/Output
    message = Message(subject="邮箱注册验证码", recipients=[email],
                      body=f"the content is about a captcha code which is:{captcha}")
    mail.send(message)
    # 缓存验证码方式：memcached/redis
    # 使用数据库方法进行存储，缺点是比较慢，没有使用缓存的方式好，只是小体量的暂代方案，即数据库暂存；
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # 需要返回RESTful API一种json格式配置
    # {code: 200/400/500, message: "", data: {}}
    return jsonify({"code": 200, "message": "", "data": None})


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")