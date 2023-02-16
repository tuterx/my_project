from functools import wraps
from flask import g, redirect, url_for


def login_required(func):
    # 保留func的信息
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))

    return inner

# 装饰器实现效果

# @login_required
# def public_question(question_id):
#     pass


# 上述装饰器实现等价于： login_required(public_question)(question_id)
