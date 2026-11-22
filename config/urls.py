
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def home(request):
    return JsonResponse({
        "name": "Zenvora ERP",
        "version": "1.0.0",
        "status": "Running successfully",
        "message": "Welcome to Zenvora ERP"
    })


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/core/", include("core.urls")),
]

