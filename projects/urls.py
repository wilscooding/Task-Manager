from django.urls import path
from .views import project_view


urlpatterns = [
    path('projects/', project_view, name='list_projects'),

]
