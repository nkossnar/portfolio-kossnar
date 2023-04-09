# pages/urls.py
from django.urls import path
from .views import home_page_view, home

urlpatterns = [
    path("", home, name="home"),
]