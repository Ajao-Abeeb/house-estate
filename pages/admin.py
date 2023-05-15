from django.contrib import admin
from  .models import Agent , Testimony , Blog
from django.utils.html import format_html
# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','phone_number','email','is_features')
    list_filter=('first_name',)
    list_display_links=('id','first_name',)
    list_editable = ('is_features',)
    search_fields = ('first_name',)
    

admin.site.register(Agent, AgentAdmin)

class TestimonyAdmin(admin.ModelAdmin):
    def thumbmail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%; " />'.format(object.image.url))
    thumbmail.short_description = 'photo'
    list_display = ('id','thumbmail','name')
    list_display_links = ('id','thumbmail','name')

admin.site.register(Testimony, TestimonyAdmin)

class  BlogAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Blog, BlogAdmin)
