class RelationClass(object):
    def __init__(self, model):
        self.instance = model()

    def get_all(self):
        return self.instance.get_query()

    def find_by_user(self, query, user_id_list):
        return self.instance.find_by_user(query, user_id_list)

    def get_some(self, query, offset, limit):
        return self.instance.get_some(query, offset, limit)
