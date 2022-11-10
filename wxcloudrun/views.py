from flask import render_template, request
from run import app
from wxcloudrun.dao import insert_userinfo, query_userinfobyphonenumber
from wxcloudrun.model import UserInfo
from wxcloudrun.response import make_succ_response


def get_has(m):
    '''
    加密算法
    :param m: 加密字符
    :return: 加密结果
    '''
    import hashlib
    p = hashlib.md5()
    p.update(m.encode("utf8"))
    return p.hexdigest()


@app.route('/login', methods=['POST'])
def login():
    """
    登录接口
    :return: 返回登录状态 1登陆成功 -1用户未注册 0密码错误
    """
    phonenumber = request.values.get('phonenumber')
    userinfo = query_userinfobyphonenumber(phonenumber)
    if userinfo:
        if get_has(request.values.get('password')) == userinfo.password:
            return make_succ_response(1, "登陆成功！")
        else:
            return make_succ_response(0, "密码错误！")
    return make_succ_response(-1, "用户未注册！")


@app.route('/register', methods=['POST'])
def register():
    """
    注册接口
    :return: 返回注册状态 1注册成功 0存在相同用户
    """
    phonenumber = request.values.get('phonenumber')
    if not query_userinfobyphonenumber(phonenumber):
        user = UserInfo(phonenumber=phonenumber, password=get_has(request.values.get('password')))
        insert_userinfo(user)
        return make_succ_response(1, "注册成功！")
    return make_succ_response(0, "存在相同用户！")
