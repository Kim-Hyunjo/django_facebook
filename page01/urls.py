from django.urls import path
from . import views

urlpatterns = [
    path('play',views.play,name = 'play'),
    path('play2',views.play2,name = 'play2'),
]
