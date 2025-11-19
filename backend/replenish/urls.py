from django.contrib import admin
from django.urls import path, include, re_path
from django.http import JsonResponse
from django.views.generic import TemplateView


# Define a simple view function (can be placed in any app's views.py or here)
# def health_check(request):
#     return JsonResponse({"status": "ok", "message": "Backend is running"})

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include('api.urls')),
path("api/auth/", include("authentication.urls")),
#path("", health_check, name="root_status"), # This catches the root path '/'
re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html'), name='index'),
]