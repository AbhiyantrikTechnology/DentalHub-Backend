from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager)
from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4


def keygenerator():
    uid = uuid4()
    return uid.hex.upper()


class UserManager(BaseUserManager):
    def create_user(self,username,email, password=None, is_active=True, is_staff=False,is_admin=False):
        if not username:
            raise ValueError(_("Users must have username."))
        if not password:
            raise ValueError(_("User must have a password."))
        user_obj = self.model(
            username = username
        )
        user_obj.password = password
        user_obj.email = email
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    # def create_staffuser(self,username, password=None):
    #     user = self.create_user(username, password, is_staff=True)

    def create_superuser(self,username, email,password=None):
        user = self.create_user(username,email, password, is_staff=True, is_admin=True)


class User(AbstractBaseUser):
    id = models.CharField(max_length=200,primary_key=True, default=keygenerator, editable=False)
    username = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100,default='admin')
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    image = models.FileField(upload_to='profile',default="profile/default-avatar.png")
    email = models.EmailField(max_length=255, null=True)

    USERNAME_FIELD = 'username'
    update_password=True

    REQUIRED_FIELDS = ['email']

    objects = UserManager()



    def save(self, *args, **kwargs):
        if (self.admin!='True' and self.update_password):
            self.set_password(self.password)
        user= super(User, self).save(*args, **kwargs)


    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.staff

    @property
    def full_name(self):
        if self.middle_name is None :
            return "%s %s" %(self.first_name,self.last_name)
        else:
            return "%s %s %s" %(self.first_name,self.middle_name,self.last_name)


    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def notification_count(self):
        return self.notification_set.filter(status=True).count()
