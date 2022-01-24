from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog

class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title', 'id')
    list_display_links = ('title', 'id' )


admin.site.register(Blog, BlogAdmin)
