# -*- coding:utf-8 -*-
from django.contrib.auth.models import Permission
import pytest
from faker import Faker
from mixer.backend.django  import mixer
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from userapp.models import User
from patientapp.models import Patient
from addressapp.models import Geography, ActivityArea

pytestmark = pytest.mark.django_db
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
fake = Faker()


class TestPatientListView(TestCase):
    def test_list_patient(self):
        client = APIClient()
        # un authorized access by user
        response = client.post('/api/v1/patients')
        assert response.status_code == 401, 'Un authorized access denied.'

        # authorized user
        user_obj = mixer.blend(User)
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = client.get('/api/v1/patients',format='json')
        print(response)
        assert response.status_code == 204, 'patients content not found'

        # authorized user
        user_obj = mixer.blend(User,admin=True)
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = client.get('/api/v1/patients',format='json')
        print(response)
        assert response.status_code == 200, 'patients list for admin'

        # # authorized user
        # user_obj = mixer.blend(User)
        # geography_obj = mixer.blend(Geography)
        # activityarea_obj = mixer.blend(ActivityArea)
        # patients_obj = mixer.blend(Patient,author=user_obj,geography=geography_obj,activity_area=activityarea_obj)
        # payload = jwt_payload_handler(user_obj)
        # token = jwt_encode_handler(payload)
        # client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        # response = client.get('/api/v1/patients',format='json')
        # print(response)
        # assert response.status_code == 200, 'patients list for users'

    def test_post_patient(self):
        activityarea_obj = mixer.blend(ActivityArea)
        geography_obj = mixer.blend(Geography)
        client = APIClient()

        # un authorized access by user
        response = client.post('/api/v1/patients')
        assert response.status_code == 401, 'Un authorized access denied.'

        # authorized user
        user_obj = User.objects.create(email=fake.email(),\
            first_name=fake.name(),last_name=fake.name())
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = client.post('/api/v1/patients', {'first_name':fake.name(),\
            'last_name':fake.name(),'gender':'male','dob':'1996-03-21',\
            'phone':"2312164654",'education':'bachelor',\
            'author':str(user_obj),'latitude':'12',\
            'longitude':'21','country':fake.name(),\
            'city':fake.name(),'state':fake.name(),\
            'street_address':fake.name(),'ward':12,\
            'activityarea_id':str(activityarea_obj.id),\
            'geography_id':str(geography_obj.id),
            'id':fake.name(),
            'middle_name':fake.name(),
            'marital_status':'single'},format='json')
        assert response.status_code == 200, 'patients created'


        # serializers error
        user_obj = User.objects.create(email=fake.email(),\
            first_name=fake.name(),last_name=fake.name())
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = client.post('/api/v1/patients', {'first_name':'',\
            'last_name':fake.name(),'gender':'male','dob':'1996-03-21',\
            'phone':"2312164654",'education':'bachelor',\
            'author':str(user_obj),'latitude':'12',\
            'longitude':'21','country':fake.name(),\
            'city':fake.name(),'state':fake.name(),'street_address':fake.name(),'ward':12},format='json')
        assert response.status_code == 400, 'serializers error'

