from django.shortcuts import render
from django.views.generic import DetailView
from .models import Departement
# Create your views here.
class DepartementDetailView(DetailView):
  model = Departement
  def get(self):
  	return HttpResponse(dumps(self.object.json()) )
