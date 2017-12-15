import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean
from sqlalchemy import ForeignKey
from DB.mysql.base_model import BaseModel


class OHHORecordExclude(BaseModel):
    __tablename__ = "ohho_record_exclude"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    exclude_user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    # match_condition_id = Column(Integer, ForeignKey("ohho_record_match_condition.id", ondelete='CASCADE', onupdate='CASCADE'))
