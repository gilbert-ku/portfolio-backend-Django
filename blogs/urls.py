from django.urls import path

from blogs.views import BlogsIndex, BlogView

urlpatterns = [
    path("", BlogsIndex.as_view()),
    path("Blogs/", BlogView.as_view()),
    # path('Blog/<int:id>/', BlogsView.as_view()),
]