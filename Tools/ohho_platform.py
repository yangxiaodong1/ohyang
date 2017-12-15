import platform


class OHHOPlatform(object):
    @staticmethod
    def is_windows():
        return platform.system() == "Windows"

    @staticmethod
    def is_linux():
        return platform.system() == "Linux"
