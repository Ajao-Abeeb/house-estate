from django.contrib import admin
from .models import Property
from django.utils.html import format_html

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    def thumbmail(self,object):
          return format_html('<img src="{}" width="40" style="border-radius: 50%; " />'.format(object.photo.url))
    thumbmail.short_description = 'photo'
    list_display = ('id','title','thumbmail', 'status' ,'is_features')
    list_display_links = ('title', 'id')
    list_editable = ('is_features',)
    search_fields = ('status','title')

admin.site.register(Property, PropertyAdmin)
