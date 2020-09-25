from django.contrib.auth.models import Group, Permission

from rest_framework import serializers

from addressapp.models import Address,Ward,Municipality,District

class WardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ward
		fields = ['id','ward','name']


class MunicipalitySerializer(serializers.ModelSerializer):
	wards = WardSerializer(source='ward_set',many=True, read_only=True)
	class Meta:
		model = Municipality
		fields = ['id','name', 'category', 'wards']

	@staticmethod
	def setup_eager_loading(queryset):
		""" Perform necessary eager loading of data. """
		queryset = queryset.select_related('wards')
		return queryset

class DistrictSerializer(serializers.ModelSerializer):
	municipalities = MunicipalitySerializer(source='municipality_set',many=True, read_only=True)

	class Meta:
		model = District
		fields = ['id','name','municipalities']

	@staticmethod
	def setup_eager_loading(queryset):
		""" Perform necessary eager loading of data. """
		queryset = queryset.select_related('municipalities')
		return queryset



class MunicipalitySerializer1(serializers.ModelSerializer):
	class Meta:
		model = Municipality
		fields = ['name',]


class GeoSerializer(serializers.ModelSerializer):
	municipality = MunicipalitySerializer1(read_only=True)
	class Meta:
		model = Ward
		fields = ['id','district','municipality','ward','location']


class WardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ward
		fields = ('id','location','district','municipality_name','ward','name','status')

class WardSerializerUpdate(serializers.ModelSerializer):
	class Meta:
		model = Ward
		fields = ('id','name')
