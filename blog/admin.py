from django.contrib import admin
from .models import Blog, Comment
from django.utils.html import format_html

# Register your models here.
class  BlogAdmin(admin.ModelAdmin): 
    def thumbmail(self,object):
          return format_html('<img src="{}" width="40" style="border-radius: 50%; " />'.format(object.image.url))
    thumbmail.short_description = 'photo'
    list_display = ('id','title','thumbmail', 'is_features')
    list_display_links = ('id', 'title', 'thumbmail', )
    list_editable = ('is_features',)
    search_fields = ('title', )

admin.site.register(Blog, BlogAdmin)




class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','comment','status',)
    list_display_links= ( 'status' , 'name')
admin.site.register(Comment, CommentAdmin)

