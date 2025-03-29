from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("text/", include("text_processor.urls", namespace="text_processor")),
    path("pesel/", include("pesel_validator.urls", namespace="pesel_validator")),
]
