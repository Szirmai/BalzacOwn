from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from creationboard import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('auth/', include('loginsystem.urls')),
    path('creationboard/', include('creationboard.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    # path('captcha/', include('captcha.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
