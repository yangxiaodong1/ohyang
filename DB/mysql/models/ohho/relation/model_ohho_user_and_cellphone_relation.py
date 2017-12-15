import datetime
import time
from sqlalchemy import Column, Boolean, Integer, DateTime, BigInteger, ForeignKey
from DB.mysql.base_model import BaseModel


class OHHOUserAndCellphoneRelation(BaseModel):
    __tablename__ = "ohho_user_and_cellphone_relation"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    cellphone_id = Column(Integer, ForeignKey("cellphone.id", ondelete='CASCADE', onupdate='CASCADE'))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    state = Column(Integer, default=1)
