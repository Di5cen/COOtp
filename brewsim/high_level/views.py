from django.shortcuts import render
from django.views.generic import DetailView
from django.http import JsonResponse 
from .models import Departement
# Create your views here.
class DepartementDetailView(DetailView):
  model = Departement
  
  def get(self,request,*args,**kwargs):
      #return HttpResponse(dumps(model.object.first().json()) )
      departement_id=kwargs.get('id_departement')
      json_data=Departement.objects.filter(id=departement_id)[0].json()
      return JsonResponse(json_data)
      
      
