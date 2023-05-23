from django.shortcuts import render , get_object_or_404
from .models import Agent 
from property.models import Property
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def agent (request):
    agent = Agent.objects.all()
    paginator = Paginator(agent, 6)
    page = request.GET.get('page')
    paged_agent = paginator.get_page(page)
    data = {
        'agent':paged_agent,
    }
    return render(request, 'agent/agent.html',data)

def agent_single(request , id):
    agent_single = get_object_or_404(Agent, pk=id)
    property = Property.objects.all()
    data = {
        'agent_single':agent_single,
        'property':property
    }
    return render(request, 'agent/agent_single.html', data)

