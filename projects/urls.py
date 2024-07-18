from django.urls import path

from projects.views import ProjectsView

urlpatterns = [
    
    path("Projects/", ProjectsView.as_view()),
    path('project/<int:id>/', ProjectsView.as_view()),
]

