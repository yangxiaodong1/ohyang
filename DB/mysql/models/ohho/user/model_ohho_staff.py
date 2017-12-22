import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel
from sqlalchemy.orm import relationship, backref
from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode


class OHHOStaff(BaseModel):
    __tablename__ = "ohho_staff"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    username = Column(String(32), unique=True)  # 手机号， 可以更改
    password = Column(String(128))

    first_name = Column(String(32), default=None)
    last_name = Column(String(32), default=None)

    cellphone = Column(String(20), default=None)
    email = Column(String(20), default=None)
    last_login = Column(DateTime, default=datetime.datetime.utcnow())

    country_code_id = Column(Integer, ForeignKey("ohho_country_code.id", ondelete='CASCADE', onupdate='CASCADE'))
    country_code = relationship("OHHOCountryCode")
    staff_accuracy_extensions = relationship("OHHOStaffAccuracyExtension", backref=backref("ohho_user", uselist=False))
    state = Column(Integer, default=1)
