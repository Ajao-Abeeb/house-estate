from django.contrib import admin
from  .models import Testimony  
from django.utils.html import format_html
# Register your models here.


class TestimonyAdmin(admin.ModelAdmin):
    def thumbmail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%; " />'.format(object.image.url))
    thumbmail.short_description = 'photo'
    list_display = ('id','thumbmail','name')
    list_display_links = ('id','thumbmail','name')

admin.site.register(Testimony, TestimonyAdmin)

