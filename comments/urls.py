from django.urls import path

from comments.views import CommentsView
urlpatterns = [
    # path("", BlogsIndex.as_view()),
    path("Comments/", CommentsView.as_view()),
    path('Comment/<uuid:pk>/', CommentsView.as_view()),
]