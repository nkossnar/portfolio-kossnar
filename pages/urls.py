# pages/urls.py
from django.urls import path
from .views import home_page_view, home, react, contact

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("react/", home, name="home"), #old orange site
    path("", react, name="react"), #new homepage
    path('sentry-debug/', trigger_error), #force sentry bug message
    #path('contact/', contact, name='contact') #test django contact form
]