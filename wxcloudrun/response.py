import json

from flask import Response


def make_succ_response(code=1, msg='success'):
    data = json.dumps({'code': code, 'msg': msg})
    return Response(data, mimetype='application/json')
