from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'adaptiv')
    # fields = ('id', 'title', 'adaptiv')
    list_display_links = ['title']
    list_editable = ['adaptiv']

admin.site.register(Project, ProjectAdmin)