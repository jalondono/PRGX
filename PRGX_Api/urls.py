from django.contrib import admin
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from sum import views


urlpatterns = [
    path('api/v1/url', views.operation_url),
    path('api/v1/body', views.operation_body),
]
