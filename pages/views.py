from django.shortcuts import render
from .models import Agent ,Testimony , Blog

# Create your views here.
def home(request):
    testimony = Testimony.objects.all()
    agent = Agent.objects.order_by("-created_date").filter(is_features=True)
    blog = Blog.objects.order_by("-created_date").filter(is_features = True)
    data ={
        'agent':agent,
        'testimony': testimony,
        'blog': blog,
    }
    return render(request,'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')
def blog(request):
    return render(request ,'pages/blog_grid.html')
def agent(request):
    agent = Agent.objects.all()
    data = {
        'agent':agent
    }
    return render(request, 'pages/agent.html',data)
def contact(request):
    return render(request, 'pages/contact.html')
def agent_single(request):
    return render(request, 'pages/agent_single.html')