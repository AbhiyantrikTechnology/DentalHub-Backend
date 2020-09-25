# -*- coding:utf-8 -*-
from django.conf.urls import include
from django.urls import path
from patientapp.api.patient import PatientListView,PatientAdd,PatientUpdateView,\
GeographyPatientListView


app_name = 'patientapp'

urlpatterns = [
	path('patients/<int:geography_id>', PatientListView.as_view(), name='user-list'),
	path('patients', PatientAdd.as_view()),
	path('accesspatients',GeographyPatientListView.as_view()),
	path('patient/<patient_id>',PatientUpdateView.as_view()),
    ]
