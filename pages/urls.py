# pages/urls.py
from django.urls import path
from .views import home_page_view, home, react

urlpatterns = [
    path("", home, name="home"),
    path("react/", react, name="react"),
]