import config
import re
from flask import g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

from wxcloudrun import auth

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


def generate_auth_token(phonenumber):
    '''
    生成token
    :param phonenumber:
    :param expiration:
    :return:
    '''
    s = Serializer(config.SERECT_KEY, expires_in=config.EXPIRATION)

    return s.dumps({'phonenumber': phonenumber})


def verify_auth_token(token):
    '''
    解析token
    :param token:
    :return:
    '''
    s = Serializer(config.SERECT_KEY)
    try:
        data = s.loads(token)
        return data
    # token过期
    except SignatureExpired:
        return None
    # token错误
    except BadSignature:
        return None


@auth.verify_password
def verify_password(token, _):
    data = verify_auth_token(token)
    if not data:
        return False
    return True
