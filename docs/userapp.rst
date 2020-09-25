============
UserAction
============
1. **METHOD:**
1. **URL:** `list all users <api/v1/users>`_

GET:
::
    api/v1/users

    - This method list all the users:

1. **METHOD:**
1. **URL:** `create a users <api/v1/users>`_

POST:
::
    api/v1/users
    
    - This method is used to create a user:

    

    **Body_Content**
- first_name: string(required)
- last_name: string(required)
- middle_name: string()
- username: String(required)
- image: ImageField(required)
- password:CharField(required)


=====================
ForgetPasswordAction
=====================
1. **METHOD:**
1. **URL:** `ForgetPassword <api/v1/users/forgetpassword>`_

POST:
::
    api/v1/users/forgetpassword
    
    - This Method is used to request for forgetpassword:

**Body_Content**

- email: Email(required)



====================
ResetPasswordAction
====================

1. **METHOD:**
1. **URL:** `Resetpassword <api/v1/users/resetpassword>`_

POST:
::
    api/v1/users/resetpassword
    
    - This Method is used for reset a password:

**Body_Content**

- token: String(required)
- password: String(required)
- confirm_password: String(required)



===============
ProfileAction
===============

1. **METHOD:**
1. **URL:** `profile of user <api/v1/profile>`_

GET:
::
    api/v1/profile

    - This method list the profilr of user:


====================
UpdateProfileAction
====================
1. **METHOD:**
1. **URL:** `update user profile <api/v1/profile/update>`_

POST:
::
    api/v1/profile/update
    
    - This method is used to update a profile of user:

    **Body_Content**

- image: ImageField(required)




=====================
ChangePasswordAction
=====================

1. **METHOD:**
1. **URL:** `ChangePassword <api/v1/users/changepassword>`_

POST:
::
    api/v1/users/changepassword
    
    - This method is used to change a password:

    **Body_Content**

- old_password: string(required)
- new_password: string(required)
- confirm_password: string(required)




