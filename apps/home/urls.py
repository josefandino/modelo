from django.urls import path
from .views import VistaIndex

urlpatterns = [
   path('', VistaIndex.as_view(), name='index')
]