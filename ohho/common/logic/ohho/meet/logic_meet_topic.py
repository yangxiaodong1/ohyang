from ohho.common.db.ohho.meet.db_ohho_topic import DBOHHOTopic
from ohho.common.logic.common.result import Result
from Tools.ohho_random import OHHORandom


class LogicMeetTopic(object):
    def __init__(self):
        self.topic = DBOHHOTopic()

    def meet_topic(self):
        query = self.topic.get_query()
        count = self.topic.get_count(query)
        if count > 0:
            index = OHHORandom.get_some_number(count)
            instance = query[index]
            if instance:
                result = Result.result_success()
                result["information"] = self.topic.get_information(instance)
            else:
                result = Result.result_failed()
                result["information"] = dict()
        else:
            result = Result.result_failed()
            result["information"] = dict()
        return result
