"""dental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token
)
from userapp.api.user import CustomAuthToken
from .seed import seed
from .views import home

admin.site.site_header = "Dental Hub  @Abhiyantrik"
admin.site.site_title = "DentalHub Admin Portal"
admin.site.index_title = "Welcome to DentalHub Admin Portal"



urlpatterns = [
    path('maintainer/', admin.site.urls),
    path('api/v1/auth', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/v1/devices', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    path('api/v1/token', obtain_jwt_token),
    path('api/v1/token/obtain', CustomAuthToken.as_view()),
    path('api/v1/token/refresh', refresh_jwt_token),
    path('api/v1/token/verify', verify_jwt_token),
    path('api/v1/',include('dental.apiurls')),
    path('seed', seed,name='seed'),
    path('', home,name='home')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns+=static(settings.DOCS_URL, document_root=settings.DOCS_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
