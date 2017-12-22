import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, SmallInteger, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Float
from DB.mysql.models.model_area import Area
from DB.mysql.base_model import BaseModel
from DB.mysql.models.ohho.base.model_ohho_body_type import *
from DB.mysql.models.ohho.base.model_ohho_industry import *
from DB.mysql.models.ohho.base.model_ohho_work_domain import *
from DB.mysql.models.ohho.base.model_ohho_profession import *
from DB.mysql.models.ohho.base.model_ohho_smoke import *
from DB.mysql.models.ohho.base.model_ohho_drink import *
from DB.mysql.models.ohho.base.model_ohho_education import *
from DB.mysql.models.ohho.base.model_ohho_school import *
from DB.mysql.models.ohho.base.model_ohho_company import *


class OHHOUserAccuracyExtension(BaseModel):
    __tablename__ = "ohho_user_accuracy_extension"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    user_id = Column(Integer, ForeignKey("ohho_user.id", ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship("OHHOUser", backref=backref("ohho_user_accuracy_extension"))

    # 必填项
    nickname = Column(String(64), default="")
    birthday = Column(Date, default=None)
    height = Column(Integer, default=0)
    sex = Column(Integer, default=0)
    occupation_id = Column(Integer, ForeignKey("ohho_interest.id", ondelete='CASCADE', onupdate='CASCADE'))
    occupation = relationship("OHHOInterest", primaryjoin="OHHOInterest.id==OHHOUserAccuracyExtension.occupation_id")
    position_id = Column(Integer, ForeignKey("ohho_interest.id", ondelete='CASCADE', onupdate='CASCADE'))
    position = relationship("OHHOInterest", primaryjoin="OHHOInterest.id==OHHOUserAccuracyExtension.position_id")
    degree_id = Column(Integer, ForeignKey("ohho_interest.id", ondelete='CASCADE', onupdate='CASCADE'))
    degree = relationship("OHHOInterest", primaryjoin="OHHOInterest.id==OHHOUserAccuracyExtension.degree_id")

    # 选填项
    identity_card = Column(String(18), default="")
    real_name = Column(String(32), default="")

    hometown = Column(String(32), default="")  # 省市
    school = Column(String(64), default="")
    company = Column(String(64), default="")
    # interest = Column(String(10240), default="")
    favourite_live_city = Column(String(64), default="")

    exclude = Column(String(1024), default="")  # the user ids that have no right to eye on me when I am online
    certification = Column(SmallInteger, default=0)  # 实名认证

    able2match = Column(Integer, default=0)
