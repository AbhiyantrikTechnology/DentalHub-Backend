# from fcm_django.models import FCMDevice
from userapp.models import User, Role
from patientapp.models import Patient
from addressapp.models import ActivityArea
from django.http import HttpResponse
from django.db.models import Sum
from django.db.models import Count
from django_seed import Seed
from faker import Faker
from mixer.backend.django  import mixer
from addressapp.models import Address, District, Municipality ,Ward
from addressapp.models import Activity
import json
fake = Faker()

def seed(request):
	try:
		User.objects.create(username='Abhiyantrik',email='abhiyantriktech@gmail.com',password='abhiyantrik123',first_name='dental',last_name='hub',admin=True,staff=True)
		Activity.objects.create(name="Health Post")
		Activity.objects.create(name="School Seminar")
		Activity.objects.create(name="Community Outreach")
		Activity.objects.create(name="Training")
		Role.objects.create(name='appuser')
		Role.objects.create(name='warduser')
		with open('./nepal.json') as write_file:
			data=json.load(write_file)
		for data_obj in data:
			district_obj1 = District.objects.create(name=data_obj['name'].capitalize())
			for muncipality_obj in data_obj['municipalities']:
				muncipality_obj1 = Municipality.objects.create(district=district_obj1,name=muncipality_obj['name'].capitalize(),category=muncipality_obj['type'])
				for i in range(1,muncipality_obj['wards']+1):
					Ward.objects.create(municipality=muncipality_obj1,ward=i)
		return HttpResponse("it works")
	except:
		return HttpResponse("Seed already done")


