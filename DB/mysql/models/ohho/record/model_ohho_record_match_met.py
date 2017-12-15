import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Numeric, ForeignKey
from DB.mysql.base_model import BaseModel


# 记录是否真实中见到过（两人都确定见到过或设备检测到见到过）
class OHHORecordMatchMet(BaseModel):
    __tablename__ = "ohho_record_match_met"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    apply_id = Column(Integer, ForeignKey("ohho_record_match_apply.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    another_user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_latitude = Column(Numeric(10, 6), default=None)
    user_longitude = Column(Numeric(10, 6), default=None)
    user_address = Column(String(64), default="")  # 用户见面时的地址
    another_user_latitude = Column(Numeric(10, 6), default=None)
    another_user_longitude = Column(Numeric(10, 6), default=None)
    another_user_address = Column(String(64), default="")  # 用户见面时的地址
    type = Column(Integer, default=1)  # 0， 设备自动检测见过； 1， 两人都点见过；
