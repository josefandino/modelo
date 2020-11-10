from django.urls import path
from .views import ViewProducts

urlpatterns = [
   path('', ViewProducts.as_view(), name='productos')
]