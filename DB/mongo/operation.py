# coding: utf-8

from DB.mongo.constant import *
from DB.mongo.connection import connect2db

db = connect2db()


class Operation(object):

    @staticmethod
    def get_db_collection(collection_name):
        return db[collection_name]

    @staticmethod
    def insert(model, document_dict):
        instance = model(document_dict)
        instance.save()

