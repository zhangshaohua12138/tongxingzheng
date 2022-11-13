from flask import render_template, request, g
from run import app
from wxcloudrun import auth
from wxcloudrun.dao import insert_userinfo, query_userinfobyphonenumber, update_userinfobyid, query_userinfobyuserid
from wxcloudrun.model import UserInfo
from wxcloudrun.response import make_succ_response, make_succ_log
import wxcloudrun.util as util


@app.route('/app/login', methods=['POST'])
def login():
    """
    登录接口
    :return: 返回登录状态 1登陆成功 -1用户未注册 0密码错误
    """
    phonenumber = request.values.get('phonenumber')

    if len(phonenumber) == 11:
        userinfo = query_userinfobyphonenumber(phonenumber)
    else:
        userinfo = query_userinfobyuserid(phonenumber)
    if userinfo:
        if util.get_has(request.values.get('password')) == userinfo.password:
            return make_succ_log(token=util.generate_auth_token(phonenumber).decode('utf-8'), code=1, msg="登陆成功！")
        else:
            return make_succ_response(0, "密码错误！")
    return make_succ_response(-1, "用户未注册！")


@app.route('/app/registerUser', methods=['POST'])
def register():
    """
    注册接口
    :return: 返回注册状态 1注册成功 0存在相同用户
    """
    phonenumber = request.values.get('phonenumber')
    if not query_userinfobyphonenumber(phonenumber):
        user = UserInfo(phonenumber=phonenumber, password=util.get_has(request.values.get('password')))
        insert_userinfo(user)
        return make_succ_response(1, "注册成功！")
    return make_succ_response(0, "存在相同用户！")


@app.route('/app/forget', methods=['POST'])
def forget():
    """
    忘记密码
    :return: 返回查询状态， 1存在用户 0该用户不存在
    """
    phonenumber = request.values.get('phonenumber')
    if query_userinfobyphonenumber(phonenumber):
        return make_succ_response(1, "查询成功！")
    return make_succ_response(0, "该用户不存在！")


@app.route('/app/resetPassword', methods=['POST'])
def resetPassword():
    """
    重置密码
    :return: 返回查询状态， 1修改成功 0修改失败
    """
    phonenumber = request.values.get('phonenumber')
    password = request.values.get('password')
    userinfo = query_userinfobyphonenumber(phonenumber)
    userinfo.password = util.get_has(password)
    update_userinfobyid(userinfo)
    return make_succ_response(1, "修改成功！")

@app.route('/app/index', methods=['POST'])
@auth.verify_password
def index():
    return make_succ_response(1, "修改成功！")