"""facebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from page01.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kimhyunjo/profile/index/',index),
    path('kimhyunjo/profile/',include('page01.urls')),
    path('event/',event),
    path('fail/',fail),
    path('warn/',warn),
    path('help/',help),
    path('/',newsfeed),
    path('feed/<pk>/',detail_feed),
    path('pages/',pages),
    path('new/',new_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('feed/<pk>/delete/', delete_feed),
    path('pages/new/', new_page),
    path('pages/<pk>/edit/', edit_page),
    path('pages/<pk>/delete/', delete_page),
]
