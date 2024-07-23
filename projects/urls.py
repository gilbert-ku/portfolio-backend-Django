from django.urls import path

from projects.views import ProjectsView, ProjectIndex

urlpatterns = [
    path("", ProjectIndex.as_view()),
    path("Projects/", ProjectsView.as_view()),
    path('Project/<uuid:pk>/', ProjectsView.as_view()),
]

