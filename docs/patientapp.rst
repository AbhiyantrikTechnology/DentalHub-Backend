===============
PatientsAction
===============

1. **METHOD:**
1. **URL:** `list a patient <api/v1/patients>`_

GET:
::
  api/v1/patients
  
  - This method list all the patients:

2. **METHOD:**
1. **URL:** `list a patient with geography_id  <api/v1/patients/geography_id>`_

GET:
::
  api/v1/patients/<geography_id

  - geography_id must be as a parameter

  - This method list all the patients of the required geography area:
  
  

3. **METHOD:**
1. **URL:** `create or register a patient <api/v1/patients>`_

POST:
::
  api/v1/patients

- This method is used to register a patients:

    **Body_Content**

- id : string()
- geography_id: string(required)
- activityarea_id : string(required)
- first_name: string(required)
- last_name: string(required)
- middle_name: string()
- gender: choicefield(required)
  male, female. other
- dob(date of birth): DateTimeField(required)
- phone(phone number):CharField(required)
- author : ForeignRelationship()
- date : autofield()
- latitude: DecimalField(required)
- longitude: DecimalField(required)
- ward_id : foreignkey(required) 
- municipality_id: foreignkey(required)
- district_id: foreignkey(required)
- education: CharField(required)
- created_at: DateField(required)
- author : Foreigne Key(User)
- recall_time : TimeField(optional)
- recall_geography : ForeigneKey(optional)


4. **PUT:**
1. **URL:** `update a patient <api/v1/patient/patient_id>`_

PUT:
::
  api/v1/patient/<patient_id>

  - patient_id must be as a parameter
  
  - This method is used to update a patients:

    **Body_Content**

- id : string()
- geography_id: string(required)
- activityarea_id : string(required)
- first_name: string(required)
- last_name: string(required)
- middle_name: string()
- gender: choicefield(required)
  male, female. other
- dob(date of birth): DateTimeField(required)
- phone(phone number):CharField(required)
- author : ForeignRelationship()
- date : autofield()
- latitude: DecimalField(required)
- longitude: DecimalField(required)
- ward_id : foreignkey(required) 
- municipality_id: foreignkey(required)
- district_id: foreignkey(required)
- education: CharField(required)
- updated_by: DateField(required)
- updated_by : Foreigne Key(User)
- recall_time : TimeField(optional)
- recall_geography : ForeigneKey(optional)