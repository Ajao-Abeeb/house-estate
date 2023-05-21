from django.shortcuts import render , get_object_or_404
from .models import Property

# Create your views here.
def property(request):
    property = Property.objects.all()
    data = {
        'property':property
    }
    return render(request, 'property/property.html' , data)
def propert_single(request, id):
    property_single = get_object_or_404(Property , pk=id )
    data = {
        'property_single':property_single
    }
    return render(request, 'property/property_single.html', data)