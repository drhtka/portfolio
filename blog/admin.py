from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_display_links = ('title', 'id' )


admin.site.register(Blog, BlogAdmin)
