from django.urls import path
from .views import ViewNosotros

urlpatterns = [
   path('', ViewNosotros.as_view(), name='nosotros')
]