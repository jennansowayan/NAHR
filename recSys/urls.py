from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_rules, name="store_recommend"),
 

]