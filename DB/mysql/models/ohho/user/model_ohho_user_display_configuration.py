import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey, Date
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


class OHHOUserDisplayConfiguration(BaseModel):
    # 根据距离distance显示用户的某些数据
    __tablename__ = "ohho_user_display_configuration"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    distance = Column(Float, default=0)
    has_sex = Column(Integer, default=0)
    has_identity_card = Column(Integer, default=0)
    has_real_name = Column(Integer, default=0)
    has_email = Column(Integer, default=0)
    has_icon = Column(Integer, default=0)
    has_source_icon = Column(Integer, default=0)
    has_nickname = Column(Integer, default=0)
    has_birthday = Column(Integer, default=0)
    has_height = Column(Integer, default=0)
    has_weight = Column(Integer, default=0)
    has_marriage = Column(Integer, default=0)
    has_resume = Column(Integer, default=0)
    has_blood = Column(Integer, default=0)
    has_hometown = Column(Integer, default=0)
    has_current = Column(Integer, default=0)
    has_industry_id = Column(Integer, default=0)
    has_body_type_id = Column(Integer, default=0)
    has_smoke_id = Column(Integer, default=0)
    has_drink_id = Column(Integer, default=0)
    has_work_domain_id = Column(Integer, default=0)
    has_profession_id = Column(Integer, default=0)
    has_school = Column(Integer, default=0)
    has_company = Column(Integer, default=0)
    has_education = Column(Integer, default=0)
    has_interest = Column(Integer, default=0)
