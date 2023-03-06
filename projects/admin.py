from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
    )


admin.site.register(Project, ProjectAdmin)
