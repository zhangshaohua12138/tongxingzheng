from datetime import datetime

from wxcloudrun import db


# 计数表
class UserInfo(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'UserInfo'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phonenumber = db.Column(db.VARCHAR(11), nullable=False)
    password = db.Column(db.VARCHAR(255), nullable=False)
    userid = db.Column(db.VARCHAR(255))
