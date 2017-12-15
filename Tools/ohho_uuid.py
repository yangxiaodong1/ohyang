import uuid


class OHHOUUID(object):
    @staticmethod
    def get_uuid1():
        return uuid.uuid1()

    @staticmethod
    def get_uuid1_string():
        source = str(OHHOUUID.get_uuid1())
        source_list = source.split("-")
        delimiter = ""
        return delimiter.join(source_list)


if __name__ == "__main__":
    print(OHHOUUID.get_uuid1())
    print(OHHOUUID.get_uuid1_string())
