from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from recruitment_management_system import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('job_portal.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)