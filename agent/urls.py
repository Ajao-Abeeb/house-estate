from django.urls import path 
from . import views

urlpatterns = [
    path('',  views.agent, name='agent'),
    path('<int:id>', views.agent_single, name='agent_single'),
]
from django.urls import path 
from . import views

 