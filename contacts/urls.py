from django.contrib import admin
from django.urls import path

from contacts.views import IndexView

urlpatterns = [
    path("index/", IndexView.as_view())
]

