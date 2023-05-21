from django.shortcuts import render , get_object_or_404
from .models import  Testimony 
from blog.models import Blog 
from agent.models import Agent
from property.models import Property
 
# Create your views here.
def home(request):
    testimony = Testimony.objects.all()
    agent = Agent.objects.order_by("-created_date").filter(is_features=True)
    blog = Blog.objects.order_by("-created_date").filter(is_features = True)
    property = Property.objects.order_by("-created_date").filter(is_features = True)
    data ={
        'agent':agent,
        'testimony': testimony,
        'blog': blog,
        'property':property
    }
    return render(request,'pages/home.html', data)

def about(request):
    agent = Agent.objects.order_by("-created_date").filter(is_features=True)
    data = {
        'agent':agent
    }
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')



