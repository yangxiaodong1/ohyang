from ohho.common.logic.common.device import Device


class LogicCancelLost(object):
    def __init__(self):
        self.device = Device()

    def cancel_lost(self, user_id, identity_id):
        return self.device.cancel_lost(user_id, identity_id)
