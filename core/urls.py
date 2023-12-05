
from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')), # linking to accounts/urls.py to core/urls.py
    path('', include('blog.urls')) # step 1. link the url
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
