import datetime
import time
from sqlalchemy import Column, String, Integer, DateTime, BigInteger, Boolean
from DB.mysql.base_model import BaseModel


class Cellphone(BaseModel):
    __tablename__ = "cellphone"
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    changed_at = Column(DateTime, default=datetime.datetime.utcnow())
    timestamp = Column(BigInteger, default=int(time.time()))

    key = Column(String(128), unique=True)  # 设备唯一标识
    operation = Column(String(64), default="")  # 设备系统
    operation_version = Column(String(64), default="")  # 设备系统版本
    manufacturer = Column(String(64), default="")  # 制造商
    brand = Column(String(64), default="")  # 品牌
    build_id = Column(String(64), default="")  # 设备版本号
    build_model = Column(String(64), default="")  # 设备名称
    platform_version = Column(String(64), default="")  # 平台版本号
    platform_type = Column(String(8), default="android")
