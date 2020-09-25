from django.db import models
from uuid import uuid4


def keygenerator():
    uid = uuid4()
    return uid.hex.upper()

class Role(models.Model):
    id = models.CharField(max_length=200,primary_key=True, default=keygenerator, editable=False)
    name = models.CharField(max_length=30,unique=True)


    def __str__(self):
    	return self.name
