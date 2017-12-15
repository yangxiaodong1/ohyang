import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOIMUserRelation(BaseModel):
    __tablename__ = "ohho_im_user_relation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    apply_id = Column(Integer, ForeignKey("ohho_record_friend_apply.id", ondelete='CASCADE', onupdate='CASCADE'),
                      default=None)
    account_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    friend_account_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    mark = Column(String(64), default="")  # 备注,用来备注朋友的真实姓名
    type = Column(Integer, default=1)  # 1好友, 2黑名单
    state = Column(Integer, default=1)
