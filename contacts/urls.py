from django.urls import path

from contacts.views import IndexView, ContactView

urlpatterns = [
    path("index/", IndexView.as_view()),
    path("contact/", ContactView.as_view()),
    path('contact/<int:id>/', ContactView.as_view()),
]

