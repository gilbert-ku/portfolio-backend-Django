from django.urls import path

from blogs.views import BlogView

urlpatterns = [
    # path("", BlogsIndex.as_view()),
    path("Blogs/", BlogView.as_view()),
    path('Blog/<uuid:pk>/', BlogView.as_view()),
]