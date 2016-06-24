"""notivinco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import verify_jwt_token

from notivinco.viewsets import * # flake8: noqa

from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

admin.autodiscover()

router = DefaultRouter()

router.register(r'users', UsersViewSet)
router.register(r'notices', NoticesViewSet)
router.register(r'comments', CommentsViewSet)

urlpatterns = [
	url(r'^api/v1/api-token-verify/',
        'rest_framework_jwt.views.verify_jwt_token'
        ),
    url(r'^api/v1/api-token-refresh/',
        'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api/v1/admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/docs/', include('rest_framework_swagger.urls')),

]