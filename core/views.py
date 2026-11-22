
from django.http import JsonResponse


def core_status(request):
    return JsonResponse({
        "application": "Zenvora Core",
        "status": "Active",
        "version": "1.0.0",
        "message": "Zenvora core application is ready"
    })
