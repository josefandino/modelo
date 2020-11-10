from django.shortcuts import render
from django.views.generic import View

class ViewNosotros(View):
   def get(self, request):
      return render(request, 'nosotros/nosotros.html')
