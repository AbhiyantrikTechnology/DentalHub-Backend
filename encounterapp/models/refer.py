from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4
from .encounter import Encounter
from userapp.models import User
import datetime



def keygenerator():
    uid = uuid4()
    return uid.hex.upper()


class Refer(models.Model):
	# id = models.CharField(max_length=200,null=True)
	id = models.CharField(max_length=200,primary_key=True, default=keygenerator, editable=False)
	no_referal = models.BooleanField(_('no referal'),default=False)
	health_post = models.BooleanField(_('health post'),default=False)
	dentist = models.BooleanField(default=False)
	general_physician = models.BooleanField(_('general physician'),default=False)
	hygienist = models.BooleanField(default=False)
	other = models.CharField(max_length=255,default="")
	encounter_id = models.OneToOneField(Encounter,on_delete=models.CASCADE,related_name='referral')
	# updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='update_refer')
	# updated_at = models.DateField(null=True)
	# created_at = models.DateField()
