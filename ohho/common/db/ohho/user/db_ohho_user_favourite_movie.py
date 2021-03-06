from DB.mysql.models.ohho.user.model_ohho_user_favourite_movie import OHHOUserFavouriteMovie
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOUserFavouriteMovie(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserFavouriteMovie, self).__init__(OHHOUserFavouriteMovie, index)

    def get_favourite_movie_list_by_user_id(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        # query = self.order_by_id_desc(query)
        query = self.order_by_index_asc(query)
        return query

    def get_by_user(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)


if __name__ == "__main__":
    pass
