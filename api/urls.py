from django.urls import path, include


urlpatterns = [
    path('Contacts/', include("contacts.urls")),
    path("Projects/", include("projects.urls")),
    path("Blogs/", include("projects.urls"))
]