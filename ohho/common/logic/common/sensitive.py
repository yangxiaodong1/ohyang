from ohho.common.db.ohho.base.db_ohho_sensitive import DBOHHOSensitive


class Sensitive(object):
    def __init__(self):
        self.sensitive = DBOHHOSensitive()

    def get_all_sensitive(self):
        return self.sensitive.get_query()

    def has_sensitive(self, content):
        sensitive_words = self.get_all_sensitive()
        for word in sensitive_words:
            temp = content.find(word)
            if temp == -1:
                continue
            else:
                return True
        return False


if __name__ == "__main__":
    pass
