from django.shortcuts import get_object_or_404, render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm


@login_required
def list_project(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/project_view.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, pk=id)
    tasks = project.tasks.all()
    context = {"project": project, "tasks": tasks}
    return render(request, "projects/show_project.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/create_project.html", context)
