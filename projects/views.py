from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required


@login_required
def project_view(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/project_view.html", context)
