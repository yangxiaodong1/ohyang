import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean, ForeignKey
from DB.mysql.base_model import BaseModel
from sqlalchemy.orm import relationship, backref
from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode


class OHHOUserFavouriteBook(BaseModel):
    __tablename__ = "ohho_user_favourite_book"
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    user_id = Column(Integer, ForeignKey("ohho_user.id", onupdate="CASCADE", ondelete="CASCADE"))
    user = relationship("OHHOUser")
    isbn = Column(String(32), default=None)
    name = Column(String(128), default=None)
    description = Column(String(1024), default=None)
    index = Column(Integer, default=0)
    icon = Column(String(256), default=None)
    url = Column(String(256), default=None)
    author = Column(String(64), default=None)
