from django.contrib import admin

# Register your models here.
from .models import Project, ProjectType

class ProjectTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(ProjectType, ProjectTypeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Project, ProjectAdmin)
