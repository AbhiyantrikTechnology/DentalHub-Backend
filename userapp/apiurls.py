# -*- coding:utf-8 -*-
from django.urls import path
from userapp.api.user import UserListView, UserForgetPassword,\
UserResetPassword, ProfileListView, UpdateUserView,\
 UserChangepassword, AdminUserCheckView, UpdateUserDataView,\
 WardCheckView,UserStatus, AdminPasswordRest
from userapp.api.role import RoleListView

# from userapp.api.staticpage import StaticPageView

app_name = 'userapp'

urlpatterns = [
	path('users', UserListView.as_view(), name='user-list'),
	path('users/forgetpassword',UserForgetPassword.as_view()),
	path('users/resetpassword',UserResetPassword.as_view()),
	path('users/changepassword',UserChangepassword.as_view()),
	path('profile', ProfileListView.as_view()),
	path('profile/update',UpdateUserView.as_view()),
	path('checkuser', AdminUserCheckView.as_view()),
	path('users/<pk>',UpdateUserDataView.as_view()),
	path('roles', RoleListView.as_view()),
	path('checkwarduser',WardCheckView.as_view()),
	path('userstatus/<user_id>',UserStatus.as_view()),
	path('adminresetpassword',AdminPasswordRest.as_view()),
    ]
