  
from mongoengine import Document, fields



class Store(Document):
    courseName = fields.StringField(required=True)
    courseCode = fields.StringField(required=True)


class StoreUpdate(Document):
    objectId = fields.StringField(required=True)
    courseName = fields.StringField(required=True)


class StoreDelete(Document):
    objectId = fields.StringField(required=True)








