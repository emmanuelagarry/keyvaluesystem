# from django.db import models
from djongo import models  
 
 
# from mongoengine import Document, EmbeddedDocument, fields

class Store(models.Model):
    courseName = models.CharField(max_length=50)
    courseCode = models.CharField(max_length=50)

    def __str__(self):
        return self.courseName



class Entry(models.Model):
    _id = models.ObjectIdField()
    courseName = models.CharField(max_length=100)
    courseCode = models.TextField()
    
    def __str__(self):
        return self.courseName

    # headline = models.CharField(max_length=255)
    # objects = models.DjongoManager()
    


# class StoreInput(EmbeddedDocument):
#     name = fields.StringField(required=True)
#     value = fields.DynamicField(required=True)

# class MyStore(Document):
#     label = fields.StringField(required=True)
#     description = fields.StringField(required=True, null=True)
#     inputs = fields.ListField(fields.EmbeddedDocumentField(StoreInput))










