from django.urls import path, include
from . import views



urlpatterns = [
    
    
    path('tech/', views.tech, name="tech"),
    path('science/', views.science, name="science"),
    path('business/', views.business, name="business"),
    path('art/', views.art, name="art"),
   
]
