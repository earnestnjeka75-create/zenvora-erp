
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "platform": "Zenvora ERP",
        "version": "1.0.0",
        "status": "running",
        "message": "Welcome to Zenvora Enterprise Platform"
    })


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
