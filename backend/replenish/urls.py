from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Define a simple view function (can be placed in any app's views.py or here)
def health_check(request):
    return JsonResponse({"status": "ok", "message": "Backend is running"})

urlpatterns = [
path('admin/', admin.site.urls),
#path('api/', include('api.urls')),
path("api/auth/", include("authentication.urls")),
path("", health_check, name="root_status"), # This catches the root path '/'
]