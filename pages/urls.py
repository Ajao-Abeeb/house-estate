from django.urls import path 
from . import views

urlpatterns = [
    path('',  views.home , name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('agent', views.agent, name='agent'),
    path('contact', views.contact , name='contact'),
    path('agent_single', views.agent_single, name='agent_single'),
    
]
