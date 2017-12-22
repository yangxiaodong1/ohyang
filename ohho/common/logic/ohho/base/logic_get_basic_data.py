from ohho.common.db.ohho.base.db_ohho_interest import *
from ohho.common.db.ohho.base.db_ohho_hint import *


class LogicGetBasicData(object):
    def __init__(self):
        self.interest = DBOHHOInterest()
        self.hint = DBOHHOHint()

    def get_interest(self):
        result = dict()
        data = self.interest.get_level_3_information(1)
        result["interest"] = data
        return result

    def parse_interest(self, interest):
        result = dict()
        result["interest"] = list()
        result["profession_id"] = list()
        result["work_domain_id"] = list()
        result["smoke_id"] = list()
        result["drink_id"] = list()
        result["other"] = list()
        interest_list = interest.get("interest", list())
        for item in interest_list:
            name = item.get("name", "")
            if name in ("书籍", "电影", "音乐", "美食", "旅行", "运动"):
                result["interest"].append(item)
            elif name == "工作内容":
                result["profession_id"].append(item)
            elif name == "行业":
                result["work_domain_id"].append(item)
            elif name == "吸烟":
                result["smoke_id"].append(item)
            elif name == "喝酒":
                result["drink_id"].append(item)
            else:
                result["other"].append(item)
        return result

    def get_hints(self):
        result = dict()
        root = self.hint.get_root()
        for item in root:
            temp = self.hint.get_by_parent_id(item.id)
            for t in temp:
                result[t.key] = t.name
        return result

    def get(self):
        result = self.get_interest()
        result = self.parse_interest(result)
        result["hints"] = self.get_hints()

        return result
