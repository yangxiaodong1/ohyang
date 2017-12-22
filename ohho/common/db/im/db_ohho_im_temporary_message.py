from DB.mysql.models.ohho.im.ohho_im_temporary_message import OHHOIMTemporaryMessage
from ohho.common.db.im.constant import *
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOIMTemporaryMessage(DBBase):
    def __init__(self):
        super(DBOHHOIMTemporaryMessage, self).__init__(OHHOIMTemporaryMessage)
