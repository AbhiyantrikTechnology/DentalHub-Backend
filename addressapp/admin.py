from django.contrib import admin

# Register your models here.
from addressapp.models import District, Municipality ,\
Ward, ActivityArea, Activity, Address
from django.utils.translation import ugettext_lazy as _

from import_export import resources

from import_export.admin import ImportExportActionModelAdmin



# class AdminGeographyapp(admin.ModelAdmin):
# 	list_display = ('id', 'tole', 'ward','status')
#
# 	def has_add_permission(self, request, obj=None):
# 		if request.user.is_superuser:
# 			return True
# 		return False
#
# 	def has_view_permission(self, request, obj=None):
# 		if request.user.is_staff or request.user.is_superuser:
# 			return True
#
# 	def has_delete_permission(self, request, obj=None):
# 		if request.user.is_superuser and request.user.is_staff:
# 			return True
# 		elif request.user.is_staff:
# 			False
#
# 	def has_change_permission(self, request, obj=None):
# 		if request.user.is_superuser and request.user.is_staff:
# 			return True
# 		elif request.user.is_staff:
# 			return False
#
# admin.site.register(Geography, AdminGeographyapp)


class DistrictResource(resources.ModelResource):
	class Meta:
		model = District
		fields = ('id', 'name', 'status')
		export_order = ('id', 'name', 'status')

class AdminDistrict(ImportExportActionModelAdmin):
	list_display = ('id', 'name', 'status')
	def has_add_permission(self, request, obj=None):
		if request.user.is_superuser:
			return True
		return False

	def has_view_permission(self, request, obj=None):
		if request.user.is_staff or request.user.is_superuser:
			return True

	def has_delete_permission(self, request, obj=None):
		if request.user.is_superuser and request.user.is_staff:
			return True
		elif request.user.is_staff:
			False

	def has_change_permission(self, request, obj=None):
		if request.user.is_superuser and request.user.is_staff:
			return True
		elif request.user.is_staff:
			return False

	resource_class = DistrictResource

admin.site.register(District, AdminDistrict)


class AdminMunicipality(admin.ModelAdmin):
	list_display = ('id', 'district', 'name','category','status')
	def has_add_permission(self, request, obj=None):
		if request.user.is_superuser:
			return True
		return False

	def has_view_permission(self, request, obj=None):
		if request.user.is_staff or request.user.is_superuser:
			return True

	def has_delete_permission(self, request, obj=None):
		if request.user.is_superuser and request.user.is_staff:
			return True
		elif request.user.is_staff:
			False

	def has_change_permission(self, request, obj=None):
		if request.user.is_superuser and request.user.is_staff:
			return True
		elif request.user.is_staff:
			return False

admin.site.register(Municipality, AdminMunicipality)



class WardResource(resources.ModelResource):
	class Meta:
		model = Ward
		fields = ('id', 'municipality__name', 'municipality__district__name', 'ward','name')
		export_order = ('id', 'municipality__name', 'municipality__district__name', 'ward','name')

class AdminWard(ImportExportActionModelAdmin):
	list_display = ('id', 'municipality', 'ward','status','name')
	def has_add_permission(self, request, obj=None):
		if request.user.is_superuser:
			return True
		return False

	def has_view_permission(self, request, obj=None):
		if request.user.is_staff or request.user.is_superuser:
			return True

	def has_delete_permission(self, request, obj=None):
		if request.user.is_superuser and request.user.is_staff:
			return True
		elif request.user.is_staff:
			False

	def has_change_permission(self, request, obj=None):
		if request.user.is_superuser and request.user.is_staff:
			return True
		elif request.user.is_staff:
			return False
	resource_class = WardResource
admin.site.register(Ward, AdminWard)

# class AdminActivity(admin.ModelAdmin):
# 	list_display = ('id', 'name')
#
# 	def has_add_permission(self, request, obj=None):
# 		if request.user.is_superuser:
# 			return True
# 		return False
#
# 	def has_view_permission(self, request, obj=None):
# 		if request.user.is_staff or request.user.is_superuser:
# 			return True
#
# 	def has_delete_permission(self, request, obj=None):
# 		if request.user.is_superuser and request.user.is_staff:
# 			return True
# 		elif request.user.is_staff:
# 			False
#
# 	def has_change_permission(self, request, obj=None):
# 		if request.user.is_superuser and request.user.is_staff:
# 			return True
# 		elif request.user.is_staff:
# 			return False
#
# admin.site.register(Activity, AdminActivity)


class AdminActivityArea(admin.ModelAdmin):
	def has_add_permission(self, request, obj=None):
		if request.user.is_superuser:
			return True
		return False

	def has_view_permission(self, request, obj=None):
		if request.user.is_staff or request.user.is_superuser:
			return True

	def has_delete_permission(self, request, obj=None):
		if request.user.is_superuser and request.user.is_staff:
			return True
		elif request.user.is_staff:
			False

	def has_change_permission(self, request, obj=None):
		if request.user.is_superuser and request.user.is_staff:
			return True
		elif request.user.is_staff:
			return False


	list_display = ('id', 'activity', 'area','status')

admin.site.register(ActivityArea, AdminActivityArea)


class AddressResource(resources.ModelResource):
	class Meta:
		model = Address
		fields = ('id', 'district', 'municipality','municipality_type','ward')
		export_order = ('id', 'district', 'municipality', 'municipality_type','ward')


# class AddressAdmin(ImportExportActionModelAdmin):
# 	list_display = ('id', 'district', 'municipality', 'municipality_type','ward')
#
# 	def has_add_permission(self, request, obj=None):
# 		if request.user.is_superuser:
# 			return True
# 		return False
#
# 	def has_view_permission(self, request, obj=None):
# 		if request.user.is_staff or request.user.is_superuser:
# 			return True
#
# 	def has_delete_permission(self, request, obj=None):
# 		if request.user.is_superuser and request.user.is_staff:
# 			return True
# 		elif request.user.is_staff:
# 			False
#
# 	def has_change_permission(self, request, obj=None):
# 		if request.user.is_superuser and request.user.is_staff:
# 			return True
# 		elif request.user.is_staff:
# 			return False
#
# admin.site.register(Address, AddressAdmin)
