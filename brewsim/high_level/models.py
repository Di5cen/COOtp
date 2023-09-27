from django.db import models

# Create your models here.

class Departement(models.Model):
  numero = models.IntergerField()
  prix = models.ForeignKey(Prix,on_delete=models.CASCADE)

class Usine(models.Mode2):
  departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
  taille = models.FloatTimeField()
  machines = models.ForeignKey(Machine,on_delete=models.PROTECT)
  recettes = models.ForeignKey(Recette,on_delete=models.PROTECT)
  stocks = models.ForeignKey(Quantiteingredient,on_delete=models.PROTECT)

class Prix(models.Mode3):
  ingredient = models.CharField()
  departement = models.CharTimeField()
  prix = models.FloatTimeField()

class Machine(models.Mode4):
  nom = models.CharField()
  prix = models.FloatTimeField()

class Recette(models.Mode5):
  nom = models.CharField()
  action = models.CharTimeField()

class Ingredient(models.Mode6):
  nom = models.CharField()

class Quantiteingredient(models.Mode7):
  ingredient = models.CharField()
  quantite = models.FloatTimeField()

class ACtion(models.Mode8):
  machine = models.CharField()
  commande = models.FloatTimeField()
  duree = models.CharTimeField()
  ingredient = models.CharTimeField()
  action = models.CharTimeField()
