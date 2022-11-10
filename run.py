# 创建应用实例
import sys

from wxcloudrun import app,db

# 启动Flask Web服务
if __name__ == '__main__':
    # app.run(host=sys.argv[1], port=sys.argv[2])
    # db.drop_all()
    # db.create_all()
    app.run()
