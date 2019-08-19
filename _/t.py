import datetime
import logging

from peewee import *

# 修改 peewee 的日志等级
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

DATABASE_CONF = {
    "host": "tk",
    "port": 3306,
    "user": "imake",
    "password": "12315",
}
db = MySQLDatabase("test", **DATABASE_CONF)


class BaseModel(Model):
    id = PrimaryKeyField()
    ctime = DateTimeField(default=datetime.datetime.now())
    utime = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db


class UserModel(BaseModel):
    name = CharField(null=True)

    class Meta:
        db_table = "tbp_user"


db.create_tables([
    UserModel
], safe=True)

if __name__ == '__main__':
    pass
