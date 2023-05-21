from django.contrib import admin
from .models import Agent 
# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','phone_number','email','is_features')
    list_filter=('first_name',)
    list_display_links=('id','first_name',)
    list_editable = ('is_features',)
    search_fields = ('first_name',)
    

admin.site.register(Agent, AgentAdmin)
