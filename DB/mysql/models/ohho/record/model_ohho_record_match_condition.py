import datetime
import time
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Date, Float, DateTime, Integer, BigInteger
from DB.mysql.base_model import BaseModel


# 记录所有用过的匹配条件
class OHHORecordMatchCondition(BaseModel):
    __tablename__ = "ohho_record_match_condition"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    sex = Column(Integer, default=None)
    email = Column(String(128), default=None)
    nickname = Column(String(64), default=None)
    birthday = Column(Date, default=None)

    big_height = Column(Float, default=None)
    small_height = Column(Float, default=None)
    big_weight = Column(Float, default=None)
    small_weight = Column(Float, default=None)
    small_age = Column(Integer, default=0)
    big_age = Column(Integer, default=150)

    marriage = Column(Integer, default=None)
    hometown = Column(String(64), default=None)
    current = Column(String(64), default=None)
    industry_id = Column(Integer, ForeignKey("ohho_industry.id", ondelete='CASCADE', onupdate='CASCADE'), default=None)
    body_type_id = Column(Integer, ForeignKey("ohho_body_type.id", ondelete='CASCADE', onupdate='CASCADE'),
                          default=None)
    smoke_id = Column(Integer, ForeignKey("ohho_smoke.id", ondelete='CASCADE', onupdate='CASCADE'), default=None)
    drink_id = Column(Integer, ForeignKey("ohho_drink.id", ondelete='CASCADE', onupdate='CASCADE'), default=None)
    work_domain_id = Column(Integer, ForeignKey("ohho_work_domain.id", ondelete='CASCADE', onupdate='CASCADE'),
                            default=None)
    profession_id = Column(Integer, ForeignKey("ohho_profession.id", ondelete='CASCADE', onupdate='CASCADE'),
                           default=None)
    label = Column(String(1024), default=None)
    interest = Column(String(1024), default=None)
