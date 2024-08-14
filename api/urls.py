from django.urls import path, include


urlpatterns = [
    path('Contacts/', include("contacts.urls")),
    path("", include("projects.urls")),
    path("Blogs/", include("blogs.urls"))
]