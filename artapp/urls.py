from django.contrib import admin
from django.urls import path
from artapp import views

app_name = 'artapp'
urlpatterns = [
    path('', views.index),  # 生命主页面请求
]
