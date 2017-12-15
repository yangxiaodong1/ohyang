import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel
from sqlalchemy.orm import relationship, backref
from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode


class OHHOUser(BaseModel):
    __tablename__ = "ohho_user"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    username = Column(String(32), unique=True)  # 手机号， 可以更改
    password = Column(String(128))
    cellphone = Column(String(20), default=None)
    last_cellphone = Column(String(20), default=None)
    country_code_id = Column(Integer, ForeignKey("ohho_country_code.id", ondelete='CASCADE', onupdate='CASCADE'))
    last_login = Column(DateTime, default=datetime.datetime.utcnow())
    state = Column(Integer, default=1)
    country_code = relationship("OHHOCountryCode")
    user_accuracy_extensions = relationship("OHHOUserAccuracyExtension", backref=backref("ohho_user", uselist=False))
