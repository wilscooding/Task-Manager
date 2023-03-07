from django.urls import path
from .views import list_project, show_project, create_project


urlpatterns = [
    path("", list_project, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
]
