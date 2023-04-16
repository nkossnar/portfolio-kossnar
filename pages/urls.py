# pages/urls.py
from django.urls import path
from .views import home_page_view, home, react

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("react/", home, name="home"),
    path("", react, name="react"),
    path('sentry-debug/', trigger_error),
]