from django.urls import path

from projects.views import ProjectsView, ProjectIndex

urlpatterns = [
    path("", ProjectIndex.as_view()),
    path("Projects/", ProjectsView.as_view()),
    path('project/<int:id>/', ProjectsView.as_view()),
]

