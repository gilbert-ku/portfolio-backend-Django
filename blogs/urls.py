from django.urls import path

from blogs.views import BlogsIndex

urlpatterns = [
    path("", BlogsIndex.as_view()),
    # path("Blogs/", BlogsView.as_view()),
    # path('Blog/<int:id>/', BlogsView.as_view()),
]