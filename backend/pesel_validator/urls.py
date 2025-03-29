from django.urls import path

from . import views

app_name = "pesel_validator"

urlpatterns = [
    path("", views.pesel_view, name="pesel_view"),
]
