import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
password = os.environ.get("MYSQL_PASSWORD", 'zhangshaohua!1')
db_address = os.environ.get("MYSQL_ADDRESS", 'sh-cynosdbmysql-grp-buzh93lg.sql.tencentcdb.com:25607')

#秘钥
SERECT_KEY = 'zhangshaohua'
EXPIRATION = 36000