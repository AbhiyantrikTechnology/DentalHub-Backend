from django.contrib.auth.models import Group, Permission

from rest_framework import serializers

from patientapp.models import Patient
from addressapp.models import ActivityArea
from addressapp.serializers.activity import ActivityAreaSerializer
from userapp.models import User


from addressapp.models import Address,Ward,Municipality,District

class WardPKField(serializers.PrimaryKeyRelatedField):
	def get_queryset(self):
		queryset = Ward.objects.all()
		return queryset


class MunicipalityPKField(serializers.PrimaryKeyRelatedField):
	def get_queryset(self):
		queryset = Municipality.objects.all()
		return queryset


class DistrictPkField(serializers.PrimaryKeyRelatedField):
	def get_queryset(self):
		queryset = District.objects.all()
		return queryset

class WardField(serializers.StringRelatedField):
	def get_queryset(self):
		queryset = Ward.objects.all()
		return queryset


class MunicipalityField(serializers.StringRelatedField):
	def get_queryset(self):
		queryset = Municipality.objects.all()
		return queryset


class DistrictField(serializers.StringRelatedField):
	def get_queryset(self):
		queryset = District.objects.all()
		return queryset

class AuthorField(serializers.PrimaryKeyRelatedField):
	def get_queryset(self):
		queryset = User.objects.all()
		return queryset


class PatientSerializer(serializers.ModelSerializer):
	activity_area = serializers.PrimaryKeyRelatedField(many=False,read_only=True,allow_null=True)
	geography = serializers.PrimaryKeyRelatedField(many=False,read_only=True,allow_null=True)
	district = serializers.PrimaryKeyRelatedField(read_only=True)
	municipality = serializers.PrimaryKeyRelatedField(read_only=True)
	ward = serializers.PrimaryKeyRelatedField(read_only=True)
	updated_by = serializers.PrimaryKeyRelatedField(read_only=True)


	activityarea_id = serializers.CharField(write_only=True,allow_null=True)
	geography_id = serializers.CharField(max_length=250,write_only=True,allow_null=True)
	district_id = DistrictPkField(many=False,write_only=True)
	municipality_id = MunicipalityPKField(many=False,write_only=True)
	ward_id = WardPKField(many=False,write_only=True)

	author = AuthorField(many=False)
	recall_geography = serializers.IntegerField(default=0)
	flag = serializers.StringRelatedField()
	class Meta:
		model = Patient
		fields = ('id','geography_id','activityarea_id','first_name', 'middle_name', 'last_name', 'full_name',\
         'gender', 'dob', 'phone','education','district','municipality', 'ward', 'district_id','municipality_id',\
         'ward_id','author', 'latitude' ,'longitude', 'date','geography','activity_area','updated_by',\
         'updated_at','created_at','recall_time','recall_geography','flag')
		read_only_fields = ('author','full_name','date','updated_at')


class PatientUpdateSerializer(serializers.ModelSerializer):
	activity_area = serializers.StringRelatedField(many=False,read_only=True)
	geography = serializers.StringRelatedField(many=False,read_only=True)
	district_id = DistrictPkField(many=False,write_only=True)
	municipality_id = MunicipalityPKField(many=False,write_only=True)
	ward_id = WardPKField(many=False,write_only=True)
	district = DistrictField(many=False,read_only=True)
	municipality = MunicipalityField(many=False,read_only=True)
	ward = WardField(many=False,read_only=True)
	updated_by = AuthorField(many=False)
	class Meta:
		model = Patient
		fields = ('id','first_name', 'middle_name', 'last_name', 'full_name',\
			'gender', 'dob','phone','education','district','municipality', 'ward',\
			'district_id','municipality_id', 'ward_id','geography','activity_area','updated_by','updated_at')
