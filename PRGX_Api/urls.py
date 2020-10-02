from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from sum import views


urlpatterns = [
    path('api/v1/', views.operation_body),
    path('api/v1/<int:a>,<int:b>', views.operation_url)
]
