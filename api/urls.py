from django.urls import path, include


urlpatterns = [
    path("", include("contacts.urls")),
    path("", include("projects.urls")),
    path("", include("blogs.urls")),
    path("", include("comments.urls"))
]