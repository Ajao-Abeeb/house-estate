from django.urls import path  
from . import views
urlpatterns = [
     path('', views.property, name='property'),
     path('<int:id>' , views.propert_single, name='property_single'),
]