import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, ForeignKey, Numeric
from DB.mysql.base_model import BaseModel


class OHHOTempMeetAddress(BaseModel):
    __tablename__ = "ohho_temp_meet_address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    apply_id = Column(Integer, ForeignKey("ohho_record_match_apply.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    latitude = Column(Numeric(10, 6), default=None)
    longitude = Column(Numeric(10, 6), default=None)
    address = Column(String(128), default="")
    name = Column(String(64), default="")
    code = Column(String(32), default="")


