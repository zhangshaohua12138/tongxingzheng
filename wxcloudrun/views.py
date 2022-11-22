from flask import render_template, request, g
from run import app
from wxcloudrun import auth
from wxcloudrun.dao import insert_userinfo, query_userinfobyphonenumber, update_userinfobyid, query_userinfobyuserid
from wxcloudrun.model import UserInfo
from wxcloudrun.response import make_succ_response, make_succ_log
import wxcloudrun.util as util
import json


@app.route('/API-APP/newsDetail', methods=['POST'])
def newsDetail():
    return_dict = {}
    return_dict['title'] = "新闻标题"
    return json.dumps(return_dict, ensure_ascii=False)
