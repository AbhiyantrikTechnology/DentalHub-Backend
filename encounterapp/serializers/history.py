from django.contrib.auth.models import Group, Permission

from rest_framework import serializers

from encounterapp.models import History


class PatientHistorySerializer(serializers.ModelSerializer):
	encounter_id = serializers.PrimaryKeyRelatedField(many=False,read_only=True)
	class Meta:
		model = History
		fields = ('id','blood_disorder','diabetes','liver_problem','rheumatic_fever',\
			'seizuers_or_epilepsy','hepatitis_b_or_c','hiv','no_allergies','allergies','other',\
			'medications', 'no_medications','no_underlying_medical_condition',\
			'not_taking_any_medications', 'encounter_id','high_blood_pressure',\
			'low_blood_pressure','thyroid_disorder')


class PatientHistoryUpdateSerializer(serializers.ModelSerializer):
	encounter_id = serializers.PrimaryKeyRelatedField(many=False,read_only=True)
	class Meta:
		model = History
		fields = ('id','blood_disorder','diabetes','liver_problem','rheumatic_fever',\
			'seizuers_or_epilepsy','hepatitis_b_or_c','hiv','no_allergies','allergies','other',\
			'medications', 'no_medications','no_underlying_medical_condition',\
			'not_taking_any_medications', 'encounter_id','high_blood_pressure',\
			'low_blood_pressure','thyroid_disorder')
