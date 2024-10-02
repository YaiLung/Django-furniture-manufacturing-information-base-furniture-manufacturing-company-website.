from . import views
from django.urls import path

urlpatterns = [

    path('', views.index),
    path('about', views.about, name= 'about'),
    path('help/', views.help, name = 'help'),
    path('what/', views.what, name = 'what'),

]
