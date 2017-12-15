import tornado.web
from Tools.ohho_operation import OHHOOperation


class ViewOHHOBase(tornado.web.RequestHandler):
    def set_format(self, format="json"):
        self._format = format

    def response(self, result_dict):
        if self._format == "api":
            return self.render("api/data.html", dict_data=result_dict)
        else:
            return self.write(OHHOOperation.dict2json(result_dict))
