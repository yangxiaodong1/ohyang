from mongoengine import Document, StringField, IntField
from DB.mongo.connection import connect2db

connect2db()


class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    username = StringField(max_length=100)
    password = StringField(max_length=100)


if __name__ == "__main__":
    u = User(first_name='leliang', last_name='li', username='lileliang', password='111111')
    u.save()
