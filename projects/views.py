from django.shortcuts import get_object_or_404, render
from .models import Project
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required
def project_view(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/project_view.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, pk=id)
    tasks = project.tasks.all()
    context = {"project": project, "tasks": tasks}
    return render(request, "projects/show_project.html", context)
