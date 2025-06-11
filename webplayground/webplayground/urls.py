from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include('pages.urls', namespace='pages')),  
    path('admin/', admin.site.urls),
]

