from django.urls import path

from contacts.views import IndexView, ContactView

urlpatterns = [
    path("", IndexView.as_view()),
    path("Contacts/", ContactView.as_view()),
    path('Contact/<int:id>/', ContactView.as_view()),
]

