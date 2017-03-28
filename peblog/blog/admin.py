from django.contrib import admin

# Register your models here.

from .models import *



class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['tag']
#    ordering = ['tag']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author','timestamp']



admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogTag,BlogTagAdmin)
