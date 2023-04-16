# contact/urls.py
from django.urls import path
from . import views
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("", views.contact_req, name="contact-reqest"), #Contact page
]