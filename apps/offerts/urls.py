from django.urls import path
from .views import ViewOfertas

urlpatterns = [
   path('', ViewOfertas.as_view(), name='ofertas')
]