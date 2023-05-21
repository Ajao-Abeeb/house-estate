from django.shortcuts import render , get_object_or_404
from .models import Agent 
# Create your views here.
def agent (request):
    agent = Agent.objects.all()
    data = {
        'agent':agent,
    }
    return render(request, 'agent/agent.html',data)

def agent_single(request , id):
    agent_single = get_object_or_404(Agent, pk=id)
    data = {
        'agent_single':agent_single,
    }
    return render(request, 'agent/agent_single.html', data)

