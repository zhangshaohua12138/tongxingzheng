import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import UserInfo

# 初始化日志
logger = logging.getLogger('log')


def query_userinfobyid(id):
    """
    根据ID查询UserInfo实体
    :param id: UserInfo的ID
    :return: UserInfo实体
    """
    try:
        return UserInfo.query.filter(UserInfo.id == id).first()
    except OperationalError as e:
        logger.info("query_userinfobyid errorMsg= {} ".format(e))
        return None


def query_userinfobyphonenumber(phonenumber):
    """
    根据phonenumber查询UserInfo实体
    :param phonenumber: UserInfo的phonenumber
    :return: UserInfo实体
    """
    try:
        return UserInfo.query.filter(UserInfo.phonenumber == phonenumber).first()
    except OperationalError as e:
        logger.info("query_userinfobyid errorMsg= {} ".format(e))
        return None

def query_userinfobyuserid(userid):
    """
    根据userid查询UserInfo实体
    :param userid: UserInfo的userid
    :return: UserInfo实体
    """
    try:
        return UserInfo.query.filter(UserInfo.userid == userid).first()
    except OperationalError as e:
        logger.info("query_userinfobyid errorMsg= {} ".format(e))
        return None

def delete_userinfobyid(id):
    """
    根据ID删除userinfo实体
    :param id: userinfo的ID
    """
    try:
        userinfo = UserInfo.query.get(id)
        if userinfo is None:
            return
        db.session.delete(userinfo)
        db.session.commit()
    except OperationalError as e:
        logger.info("delete_userinfobyid errorMsg= {} ".format(e))


def insert_userinfo(userinfo):
    """
    插入一个userinfo实体
    :param userinfo: UserInfo实体
    """
    try:
        db.session.add(userinfo)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_userinfo errorMsg= {} ".format(e))


def update_userinfobyid(userinfo):
    """
    根据ID更新userinfo的值
    :param userinfo实体
    """
    try:
        # userinfo = query_userinfobyid(userinfo.id)
        if userinfo is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_userinfobyid errorMsg= {} ".format(e))
