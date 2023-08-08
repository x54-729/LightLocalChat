from peewee import Model, CharField, DateTimeField, ForeignKeyField, AutoField
import datetime

from .utils import JSONField, BaseModel
from .user import User
from .generate_config import Generate_Config


class Dialogue_Mess(BaseModel):
    
    mess_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(User, backref='dialogue_messages') # User 表外键关联
    gen_id = ForeignKeyField(Generate_Config, backref='dialogue_messages') # Generate_Config 表外键关联
    message = JSONField()
    created_time = DateTimeField(default=datetime.datetime.now)
    session_id = CharField(unique=True) # 会话的 id

