
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls') ),
    path('ofertas', include('apps.offerts.urls') ),
    path('nosotros', include('apps.nosotros.urls') ),
    path('productos', include('apps.products.urls') ),
]
