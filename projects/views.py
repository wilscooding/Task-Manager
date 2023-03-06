from django.shortcuts import render
from .models import Project


def project_view(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/project_view.html", context)
