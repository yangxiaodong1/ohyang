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


class OHHOStaffAccuracyExtension(BaseModel):
    __tablename__ = "ohho_staff_accuracy_extension"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))
    user_id = Column(Integer, ForeignKey("ohho_staff.id", ondelete='CASCADE', onupdate='CASCADE'))
    user = relationship("OHHOStaff", backref=backref("ohho_staff_accuracy_extension"))

    # 必填项
    birthday = Column(Date, default=None)
    height = Column(Integer, default=0)
    sex = Column(Integer, default=0)
