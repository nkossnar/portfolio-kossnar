# pages/urls.py
from django.urls import path
from .views import home_page_view, home, react

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("", home, name="home"),
    path("react/", react, name="react"),
    path('sentry-debug/', trigger_error),
]