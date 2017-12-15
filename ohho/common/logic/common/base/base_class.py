class BaseClass(object):
    def __init__(self, model):
        self.instance = model()

    def add(self, data):
        return self.instance.add(data)

    def update(self, instance, data):
        return self.instance.update(instance, data)

    def get(self, instance_id):
        return self.instance.get_by_id(instance_id)

    def get_by_id(self, the_id):
        return self.instance.get_by_id(the_id)

    def get_all(self):
        query = self.instance.get_query()
        query = self.instance.order_by_id_desc(query)
        return query

    def find_by_name(self, query, name):
        return self.instance.find_by_name(query, name)

    def find_by_first(self, query,first):
        return self.instance.find_by_first(query, first)

    def find_by_second(self, query, second):
        return self.instance.find_by_second(query, second)

    def find_by_distance(self, query, distance):
        return self.instance.find_by_distance(query, distance)

    def get_some(self, query, offset, limit):
        return self.instance.get_some(query, offset, limit)

    def delete(self, instance):
        return self.instance.delete(instance)

    def restore(self, instance):
        return self.instance.restore(instance)

    def get_valid(self, query):
        return self.instance.get_valid(query)

    def get_invalid(self, query):
        return self.instance.get_invalid(query)
