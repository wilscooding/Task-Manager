from django.urls import path
from .views import project_view, show_project


urlpatterns = [
    path("projects/", project_view, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
]
