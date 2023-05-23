from django.shortcuts import render , get_object_or_404
from .models import Property
from random import choice
from agent.models import Agent

# Create your views here.
def property(request):
    property = Property.objects.all()
    data = {
        'property':property
    }
    return render(request, 'property/property.html' , data)
def propert_single(request, id):
    property_single = get_object_or_404(Property , pk=id )
    pks = Agent.objects.values_list('pk' ,flat=True)
    random_pk = choice(pks)
    random_pk_agent = Agent.objects.get(pk=random_pk)
    data = {
        'property_single':property_single,
        'random_pk_agent':random_pk_agent,
    }
    return render(request, 'property/property_single.html', data)

def search(request):
    propertys = Property.objects.order_by('-created_date')
    city_search = Property.objects.values_list('location', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            propertys =propertys.filter(title__icontains=keyword) 
    if 'location' in request.GET:
        city = request.GET['location']
        if city :
            propertys = propertys.filter(location__iexact=city)
    data = {
        'propertys':propertys,
        'city_search':city_search
    }
    return render(request ,'property/search.html', data)
 
 