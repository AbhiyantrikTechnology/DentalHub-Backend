===============
AddressAction
===============
1. **METHOD:**
**URL:** `list a address <api/v1/addresses>`_

GET:
::  
    api/v1/addresses

    - This method list all the address related to district ,municipality and ward of Nepal:


================
GeographyAction
================
1. **METHOD:**
**URL:** `list a geography <api/v1/geography>`_

GET:
::
  api/v1/geography
  
  - This method list all geography data.


2. **METHOD:**
*URL:** `create a geography <api/v1/geography>`_

POST:
::
    api/v1/geography

- This Method is used for adding a Geography:

**Body_Content**

- district: ChoiceField(required)
- municipality: ChoiceField(required)
- ward: PositiveIntegerField()


4. **Put:**
*URL:** `update a geography <api/v1/geography/geography_id>`_

POST:
::
    api/v1/geography/<geography_id>
    
    - This Method is used for updating a geography:



=================
ActivitieAction
=================
1. **METHOD:**
*URL:** `list a activities <api/v1/events>`_

GET:
::
    api/v1/events
    
    - This method list all the activitie:


=====================
ActivitieAreaAction
=====================
1. **METHOD:**
*URL:** `list a activitiesarea <api/v1/activities>`_

GET:
::
    api/v1/activities

- This method list all the activitiearea:


2. **METHOD:**
*URL:** `create a activitiesarea <api/v1/activities>`_

POST:
::
    api/v1/activities

- This Method is used for adding a activitiearea:

**Body_Content**


- activity id : ForeignKey(required) ie Activity id
- name: String()


3. **Put:**
*URL:** `update a activitiesarea <api/v1/activities/activities_id>`_

POST:
::
    api/v1/activities/<activities_id>

- activities_id: CharField (activities_id as a parameter)


- This Method is used for updating a activities:


=============
RecallAction
=============
1. **METHOD:**
*URL:** `update a activitiesarea <api/v1/recalls/geography_id>`_

GET:
::
	api/v1/recalls/<geography_id>

    - This method list all the recall for the patients:

    - this screen should be show only when health post is click in acticities section:


